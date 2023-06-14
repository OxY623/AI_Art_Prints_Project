from django.views.generic import ListView, DetailView
from .models import Article

# Определение классов-обработчиков запросов:

class NewsListView(ListView):
    model = Article               # Модель для получения списка объектов
    template_name = 'news/news_list.html'   # Шаблон для отображения списка


class NewsDetailView(DetailView):
    model = Article               # Модель для получения объекта
    template_name = 'news/news_detail.html'  # Шаблон для отображения объекта
