from django.views.generic import ListView, DetailView
from .models import Article


class NewsListView(ListView):
    model = Article
    template_name = 'news/news_list.html'


class NewsDetailView(DetailView):
    model = Article
    template_name = 'news/news_detail.html'
