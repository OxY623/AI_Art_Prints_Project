from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from prints.models import Print, Cart, CartPrint
from django.contrib import messages

@login_required
def cart_view(request):
    # Получение или создание корзины для текущего пользователя
    cart, created = Cart.objects.get_or_create(user=request.user)
    # Получение всех элементов в корзине (CartPrint) для текущего пользователя
    cart_items = cart.cartprint_set.all()
    # Вычисление общей стоимости элементов в корзине
    total_price = 0
    for item in cart_items:
        total_price += item.print.price * item.quantity
    # Отображение шаблона корзины и передача контекста с элементами корзины и общей стоимостью
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def add_to_cart(request, print_id):
    # Получение объекта печати по id
    print = get_object_or_404(Print, id=print_id)
    # Получение или создание корзины для текущего пользователя
    cart, created = Cart.objects.get_or_create(user=request.user)
    # Получение или создание элемента корзины для текущей корзины и печати
    cart_print, created = CartPrint.objects.get_or_create(cart=cart, print=print)
    if not created:
        # Если элемент уже существует в корзине - увеличиваем его количество на 1
        cart_print.quantity += 1
        cart_print.save()
    # Отображаем сообщение об успешном добавлении элемента в корзину
    messages.success(request, f"{print.title} добавлен в корзину.")
    # Перенаправляем на страницу корзины
    return redirect('cart:cart')

@login_required
def remove_from_cart(request, cart_print_id):
    # Получение объекта элемента корзины по id и убедимся, что он принадлежит текущему пользователю
    cart_print = get_object_or_404(CartPrint, id=cart_print_id, cart__user=request.user)
    # Удаление элемента корзины из базы данных
    cart_print.delete()
    # Отображаем сообщение об успешном удалении элемента из корзины
    messages.success(request, f"{cart_print.print.title} удален из корзины.")
    # Перенаправляем на страницу корзины
    return redirect('cart:cart')