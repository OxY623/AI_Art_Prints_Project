from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Print
from .forms import SearchForm, SearchPrintsForm, PrintFormCreate
from django.core.paginator import Paginator
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView
from django.http import Http404
from django.conf import settings
import os



# Вьюха для отображения списка всех Print-ов
def print_list_view(request):
    # Получаем список всех объектов из модели Print
    object_list = Print.objects.all()

    # Получаем список просмотренных объектов из сессии пользователя
    viewed = request.session.get('viewed', [])

    # Создаем объект формы и передаем GET-параметры
    form = SearchPrintsForm(request.GET)

    # Проверяем, что форма прошла валидацию
    if form.is_valid():
        # Получаем данные, введенные пользователем в форму
        date_from = form.cleaned_data.get('date_from')
        date_to = form.cleaned_data.get('date_to')
        price_from = form.cleaned_data.get('price_from')
        price_to = form.cleaned_data.get('price_to')

        # Фильтруем список объектов с помощью полученных данных
        if date_from:
            object_list = object_list.filter(created_at__gte=date_from)
        if date_to:
            object_list = object_list.filter(created_at__lte=date_to)
        if price_from:
            object_list = object_list.filter(price__gte=price_from)
        if price_to:
            object_list = object_list.filter(price__lte=price_to)

    # Разбиваем отфильтрованный список на страницы
    paginator = Paginator(object_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Добавляем объект формы и списки в контекст шаблона
    context = {
        'object_list': page_obj,
        'viewed': viewed,
        'form': form,
    }

    # Если форма не прошла валидацию, передаем ее с ошибками в контекст шаблона
    if not form.is_valid():
        context['form'] = form

    # Отображаем список Print-ов и форму поиска на странице
    return render(request, 'prints/print-list.html', context)


# Вьюха для отображения конкретного Print-а
def print_lookup_view(request, my_id):
    # Получаем объект Print с заданным id или выбрасываем 404 ошибку
    obj = get_object_or_404(Print, id=my_id)

    # Получаем список просмотренных объектов из сессии пользователя
    viewed = request.session.get('viewed', [])

    # Добавляем id просмотренного объекта в список и сохраняем его в сессии
    if obj.id not in viewed:
        viewed.append(obj.id)
        request.session['viewed'] = viewed

    # Получаем `quantity` из POST-запроса
    quantity = request.POST.get('quantity')

    # Создаем контекст шаблона для отображения определенного Print-а
    context = {
        'object': obj,
        'quantity': quantity,
    }

    # Отображаем данные Print-а на странице
    return render(request, 'prints/print-detail.html', context)


# Вьюха для поиска Print-ов по ключевому слову
def print_search_view(request):
    # Получаем ключевое слово поиска из GET-запроса
    search_text = request.GET.get('search', '')

    # Фильтруем список Print-ов, чтобы получить все объекты, содержащие заданное ключевое слово
    prints = Print.objects.filter(title__icontains=search_text)

    # Создаем контекст шаблона для отображения результатов поиска
    context = {
        'search_text': search_text,
        'prints': prints,
    }

    # Отображаем результаты поиска на странице
    return render(request, 'search.html', context)


# Вьюха для основной страницы с поиском Print-ов
def print_search_main_view(request):
    # Получаем ключевое слово поиска из GET-запроса
    search_text = request.GET.get("search", '')

    # Создаем объект формы и передаем GET-параметры
    form = SearchForm(request.GET)

    # Создаем пустой set для хранения Print-ов
    prints = set()

    # Проверяем, что форма прошла валидацию и содержит данные
    if form.is_valid() and form.cleaned_data['search']:
        # Получаем данные, введенные пользователем в форму
        search = form.cleaned_data['search']
        search_in = form.cleaned_data.get('search_in') or 'title'

        # Фильтруем список Print-ов в зависимости от параметров поиска
        if search_in == 'title':
            prints = Print.objects.filter(title__icontains=search)
        else:
            prints = Print.objects.filter(description__icontains=search)

    # Создаем контекст шаблона для отображения результатов поиска на главной странице
    context = {
        'search_text': search_text,
        'prints': prints,
    }

    # Отображаем результаты поиска на главной странице
    return render(request, 'home.html', context)


# Вьюха для отображения подробной информации о Print
def print_detail_full(request, my_pk):
    # Получаем объект Print с заданным pk или выбрасываем 404 ошибку
    print = get_object_or_404(Print, pk=my_pk)

    # Получаем список товаров из корзины из сессии пользователя и считаем общую стоимость заказа
    cart_items = request.session.get('cart', {})
    total_price = sum(item['quantity'] * item['print'].price for item in cart_items.values())

    # Создаем контекст шаблона для отображения детальной информации о товаре
    context = {
        'object': print,
        'cart_items': cart_items.values(),
        'total_price': total_price,
    }

    # Отображаем детальную информацию о товаре на странице
    return render(request, 'prints/print-detail_all.html', context)


# test views superuser funcs
# @user_passes_test(lambda u: u.is_superuser)
def edit_print_superuser(request, pk=None):
    if pk is not None:
        print_obj = get_object_or_404(Print, pk=pk)
    else:
        print_obj = None

    if request.method == 'POST':
        form = PrintFormCreate(request.POST, request.FILES, instance=print_obj)
        if form.is_valid():
            obj = form.save(commit=False)

            # Проверяем, загружена ли пользователем новая картинка.
            if request.FILES.get("image"):
                # Определяем путь к медиа-файлам и создаем его, если он не существует.
                media_root = getattr(settings, 'MEDIA_ROOT', None)
                if not media_root:
                    raise ImproperlyConfigured("MEDIA_ROOT setting must not be empty")
                path = os.path.join(media_root, 'prints')
                os.makedirs(path, exist_ok=True)
                # Сохраняем файл.
                image = request.FILES.get("image")
                filename = f"{image.name}"
                filepath = os.path.join(path, filename)
                with open(filepath, 'wb') as f:
                    for chunk in image.chunks():
                        f.write(chunk)
                obj.image = os.path.join('prints', filename)

            obj.save()
            form.save_m2m()

            if print_obj is None:
                messages.success(request, f'Принт "{obj.title}" был создан')
            else:
                messages.success(request, f'Принт "{obj.title}" был успешно обновлен')
            return redirect('prints:print_list_super')
    else:
        form = PrintFormCreate(instance=print_obj)

    context = {
        'method': request.method,
        'form': form,
    }

    return render(request, 'prints/form-edit-print.html', context)
def print_delete_view(request, id):
    print_to_delete = Print.objects.get(id=id)
    if request.method == "POST":
        print_to_delete.delete()
        return redirect('print_list')
    context = {
        'object': print_to_delete
    }
    return render(request, 'prints/print_delete_super_user.html', context)


# @user_passes_test(lambda u: u.is_superuser)
class PrintListViewSuperUser(ListView):
    model = Print
    template_name = 'prints/print_list_super_user.html' # имя шаблона для вывода списка всех принтов
    context_object_name = 'prints' # имя переменной контекста, в которой будут переданы все объекты модели "Print"

    def get_queryset(self):
        return Print.objects.all()


def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=id)
    # obj = get_object_or_404(Product, id=id)
    try:
        obj = Print.objects.get(id=id)
    except Print.DoesNotExist:
        raise Http404
    context = {
        'object': obj
    }
    return render(request, 'prints/print_super_user.html', context)


