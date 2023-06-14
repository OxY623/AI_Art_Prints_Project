import csv
#from decimal import Decimal
from django.shortcuts import render, redirect
from prints.models import Cart, CartPrint, Print
from .forms import PurchaseForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
import os
from django.conf import settings


@login_required # Декоратор проверяет, что пользователь авторизован. Если нет, то перенаправит на страницу входа.
def confirm_purchase(request):
    if request.method == 'POST': # Если метод запроса POST, т.е. форма была отправлена.
        form = PurchaseForm(request.POST) # Обработка содержимого формы POST.
        if form.is_valid(): # Проверка, что форма заполнена корректно.
            # Получение данных из формы.
            user_address = form.cleaned_data.get('address')
            user_city = form.cleaned_data.get('city')
            user_state = form.cleaned_data.get('state')
            user_country = form.cleaned_data.get('country')
            user_zip_code = form.cleaned_data.get('zip_code')

            cart = Cart.objects.filter(user=request.user).last() # Получение последней корзины пользователя из базы данных.
            cart_prints = CartPrint.objects.filter(cart=cart) # Получение списка товаров в корзине.

            order_info = {
                "user_id": request.user.id, # ID пользователя, сделавшего заказ.
                "address": user_address,
                "city": user_city,
                "state": user_state,
                "country": user_country,
                "zip_code": user_zip_code,
                "order_details": [] # Список товаров в заказе.
            }

            for item in cart_prints: # Перебор всех товаров в корзине.
                item.print.quantity -= item.quantity # Уменьшение количества товара на складе.
                item.print.save() # Сохранение изменений в базе данных.
                order_detail = {
                    "print_id": item.print.id, # ID товара.
                    "title": item.print.title, # Заголовок товара.
                    "price": float(item.print.price), # Цена товара.
                    "quantity": item.quantity # Количество товара в заказе.
                }
                order_info["order_details"].append(order_detail) # Добавление информации о товаре в список заказа.

            filename = f'order_{request.user.username}_{datetime.now().strftime("%Y-%m-%d %H.%M.%S")}.csv' # Генерация имени файла CSV с заказом.
            filepath = os.path.join(settings.BASE_DIR, 'orders', filename) # Формирование пути до файла CSV.
            with open(filepath, 'w', newline='') as f: # Открытие файла CSV для записи.
                writer = csv.writer(f)
                # Запись информации о заказе в файл CSV.
                writer.writerow(['User ID', 'Address', 'City', 'State', 'Country', 'Zip Code',
                                 'Print ID', 'Title', 'Price', 'Quantity'])
                for item in order_info["order_details"]:
                    writer.writerow([order_info["user_id"], order_info["address"], order_info["city"],
                                     order_info["state"], order_info["country"], order_info["zip_code"],
                                     item["print_id"], item["title"], item["price"], item["quantity"]])

            cart.delete() # Удаление корзины из базы данных.

            messages.success(request, 'Your order has been successfully submitted. Thank you for your purchase!') # Предупреждение об успешном оформлении заказа.
            return redirect('purchase:thank_you') # Перенаправление на страницу подтверждения заказа.

    else:
        form = PurchaseForm() # Создание объекта формы для отображения.

    context = {
        'form': form
    }

    return render(request, 'purchase/purchase.html', context) # Отображение страницы оформления заказа.


@login_required
def thank_you(request):
    return render(request, 'purchase/confirm_purchase.html') # Отображение страницы подтверждения заказа.