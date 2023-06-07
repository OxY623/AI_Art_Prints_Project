from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Print


# Create your views here.

def print_list_view(request):
    queryset = Print.objects.all()
    viewed = request.session.get('viewed', [])
    context = {
        'object_list': queryset,
        'viewed': viewed,
    }
    return render(request, 'prints/print-list.html', context)


def print_lookup_view(request, my_id):
    obj = get_object_or_404(Print, id=my_id)
    viewed = request.session.get('viewed', [])
    if obj.id not in viewed:
        viewed.append(obj.id)
        request.session['viewed'] = viewed
    # try:
    #     obj = Print.objects.get(id=my_id)
    # except Print.DoesNotExist:
    #     raise Http404
    context = {
        'object': obj,

    }
    return render(request, 'prints/print-detail.html', context)


def print_search_view(request):
    search_text = request.GET.get('search', '')
    prints = Print.objects.filter(title__icontains=search_text)

    context = {
        'search_text': search_text,
        'prints': prints,

    }
    return render(request, 'search.html', context)
