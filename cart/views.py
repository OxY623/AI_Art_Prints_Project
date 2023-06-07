from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from prints.models import Print, Cart, CartPrint
from django.contrib import messages

@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartprint_set.all()
    total_price = 0
    for item in cart_items:
        total_price += item.print.price * item.quantity
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def add_to_cart(request, print_id):
    print = get_object_or_404(Print, id=print_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_print, created = CartPrint.objects.get_or_create(cart=cart, print=print)
    if not created:
        cart_print.quantity += 1
        cart_print.save()
    messages.success(request, f"{print.title} added to cart.")
    return redirect('cart:cart')

@login_required
def remove_from_cart(request, cart_print_id):
    cart_print = get_object_or_404(CartPrint, id=cart_print_id, cart__user=request.user)
    cart_print.delete()
    messages.success(request, f"{cart_print.print.title} removed from cart.")
    return redirect('cart:cart')