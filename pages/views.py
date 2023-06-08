from django.shortcuts import render
from django.core.paginator import Paginator
from prints.forms import SearchForm
from prints.models import Print


# Create your views here.

def homeView(request):
    form = SearchForm(request.GET or None)
    search_text = request.GET.get('search', '')
    search_in = request.GET.get('search_in', 'title')

    if form.is_valid():
        search_text = form.cleaned_data.get('search')
        search_in = form.cleaned_data.get('search_in', 'title')

    prints = (Print.objects.filter(title__icontains=search_text)
              if search_in == 'title'
              else Print.objects.filter(description__icontains=search_text))

    paginator = Paginator(prints, 10)
    page_number = request.GET.get('page')
    items_page = paginator.get_page(page_number)

    context = {
        'form': form,
        'search_text': search_text,
        'prints': items_page,
    }

    return render(request, 'home.html', context)


def aboutView(request):
    return render(request, 'about.html', {})


def contactView(request):
    return render(request, 'contact.html', {})
