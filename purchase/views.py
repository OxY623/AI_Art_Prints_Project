from django.shortcuts import render, redirect
from prints.models import Cart, CartPrint, Print
from .forms import PurchaseForm
from django.contrib import messages


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

            # Отправка сообщения пользователю об успешной покупке
            messages.success(request, 'Ваш заказ принят! Спасибо за покупку.')

            # Возвращение пользователя на главную страницу
            return redirect('home')
    else:
        form = PurchaseForm()

    context = {
        'form': form
    }

    return render(request, '/purchase/purchase.html', context)