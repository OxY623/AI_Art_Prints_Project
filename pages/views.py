from django.shortcuts import render
from django.core.paginator import Paginator
from prints.forms import SearchForm
from prints.models import Print


# Определение функций-обработчиков запросов:

def homeView(request):
    # Создание объекта формы и извлечение значений полей
    form = SearchForm(request.GET or None)
    search_text = request.GET.get('search', '')
    search_in = request.GET.get('search_in', 'title')

    # Если форма действительна, сохраняем значения полей
    if form.is_valid():
        search_text = form.cleaned_data.get('search')
        search_in = form.cleaned_data.get('search_in', 'title')

    # Формирование запроса в базу данных (запрос содержит поиск текста в полях title или description)
    prints = (
        Print.objects.filter(title__icontains=search_text)
        if search_in == 'title'
        else Print.objects.filter(description__icontains=search_text)
    )

    # Создание пагинации (по 10 объектов на страницу)
    # paginator = Paginator(prints, 10)
    # page_number = request.GET.get('page')
    # items_page = paginator.get_page(page_number)

    # Создание контекста (словаря данных), передаваемого в шаблон
    context = {
        'form': form,
        'search_text': search_text,
        'prints': prints
        # 'prints': items_page,
    }

    # Отображение главной страницы (home.html) с контекстом данных
    return render(request, 'home.html', context)


def aboutView(request):
    # Отображение страницы "О нас" (about.html) с пустым контекстом
    return render(request, 'about.html', {})


def contactView(request):
    # Отображение страницы "Контакты" (contact.html) с пустым контекстом
    return render(request, 'contact.html', {})
