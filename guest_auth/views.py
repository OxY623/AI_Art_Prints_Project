from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Определение функций-обработчиков запросов:

def register_view(request):
    if request.method == 'POST':            # Если запрос - метод POST (из формы отправлены данные)
        form = UserCreationForm(request.POST)   # Создание объекта формы и передача POST-данных
        if form.is_valid():                  # Если форма действительна (заполнена корректно)
            user = form.save()               # Создание нового пользователя на основе отправленной формы
            login(request, user)             # Аутентификация пользователя
            return redirect('home')          # Перенаправление на главную страницу
    else:
        form = UserCreationForm()             # Если запрос - метод GET (отображение пустой формы)
    return render(request, 'registration/register.html', {'form': form})   # Отображение шаблона с контекстом формы

def login_view(request):
    if request.method == 'POST':            # Если запрос - метод POST (из формы отправлены данные)
        form = AuthenticationForm(data=request.POST)   # Создание объекта формы и передача POST-данных
        if form.is_valid():                  # Если форма действительна (заполнена корректно)
            user = form.get_user()           # Получение объекта пользователя на основе отправленной формы
            login(request, user)             # Аутентификация пользователя
            return redirect('home')          # Перенаправление на главную страницу
    else:
        form = AuthenticationForm()         # Если запрос - метод GET (отображение пустой формы)
    return render(request, 'registration/login.html', {'form': form})  # Отображение шаблона с контекстом формы

def logout_view(request):
    logout(request)               # Выход пользователя из системы
    return redirect('home')       # Перенаправление на главную страницу