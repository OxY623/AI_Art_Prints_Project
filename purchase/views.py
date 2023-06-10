from django.shortcuts import render, redirect
from prints.models import Cart, CartPrint, Print
from .forms import PurchaseForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages

# @login_required
# def confirm_purchase(request):
#     if request.method == 'POST':
#         form = PurchaseForm(request.POST)
#         if form.is_valid():
#             # Получение данных из формы
#             user_address = form.cleaned_data.get('address')
#             user_city = form.cleaned_data.get('city')
#             user_state = form.cleaned_data.get('state')
#             user_country = form.cleaned_data.get('country')
#             user_zip_code = form.cleaned_data.get('zip_code')
#
#             # Создание нового заказа и сохранение данных в базу данных
#             cart = Cart.objects.filter(user=request.user).last()
#             cart_prints = CartPrint.objects.filter(cart=cart)
#             for item in cart_prints:
#                 item.print.quantity -= item.quantity
#                 item.print.save()
#             cart.delete()
#
#
#
#             # Возвращение пользователя на главную страницу
#             return redirect('purchase:confirm_purchase')
#     else:
#         form = PurchaseForm()
#
#     context = {
#         'form': form
#     }
#
#     return render(request, ' purchase/purchase.html', context)



@login_required
def confirm_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            # Получение данных из формы
            user_address = form.cleaned_data.get('address')
            user_city = form.cleaned_data.get('city')
            user_state = form.cleaned_data.get('state')
            user_country = form.cleaned_data.get('country')
            user_zip_code = form.cleaned_data.get('zip_code')

            # Создание нового заказа и сохранение данных в базу данных
            cart = Cart.objects.filter(user=request.user).last()
            cart_prints = CartPrint.objects.filter(cart=cart)
            for item in cart_prints:
                item.print.quantity -= item.quantity
                item.print.save()
            cart.delete()

            # Отправка информации о подтверждении заказа на почту
            message = f'Заказ от {request.user.username}, Адрес: {user_address}, ' \
                      f'Город: {user_city}, Область/штат: {user_state}, ' \
                      f'Страна: {user_country}, Почтовый индекс: {user_zip_code}'
            print("Успех")
            send_mail('Подтверждение заказа', message, 'your_email@example.com', ['fuzzydoorproductions0@gmail.com'], fail_silently=False)

            # Возвращение пользователя на главную страницу
            return redirect('purchase:confirm_purchase')
    else:
        form = PurchaseForm()

    context = {
        'form': form
    }

    return render(request, ' purchase/purchase.html', context)

@login_required
def confirm_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            # Получение данных из формы
            user_address = form.cleaned_data.get('address')
            user_city = form.cleaned_data.get('city')
            user_state = form.cleaned_data.get('state')
            user_country = form.cleaned_data.get('country')
            user_zip_code = form.cleaned_data.get('zip_code')

            # Создание нового заказа и сохранение данных в базу данных
            cart = Cart.objects.filter(user=request.user).last()
            cart_prints = CartPrint.objects.filter(cart=cart)
            for item in cart_prints:
                item.print.quantity -= item.quantity
                item.print.save()
            cart.delete()

            # # Отправка информации о подтверждении заказа на почту
            # message = f'Заказ от {request.user.username}, Адрес: {user_address}, Город: {user_city}, Область/штат: {user_state}, Страна: {user_country}, Почтовый индекс: {user_zip_code}'
            # send_mail('Подтверждение заказа', message, 'your_email@example.com', ['fuzzydoorproductions0@gmail.com'], fail_silently=False)

            # Возвращение пользователя на главную страницу
            return redirect('purchase:confirm_purchase')
    else:
        form = PurchaseForm()

    context = {
        'form': form
    }

    return render(request, ' purchase/purchase.html', context)

@login_required
def thank_you(request):
    return render(request,' purchase/confirm_purchase.html')