from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sorter = request.GET.get('sort')
    phones_catalog = Phone.objects.all()
    if sorter == 'name':
        phones_catalog = phones_catalog.order_by('name')
    elif sorter == 'max_price':
        phones_catalog = phones_catalog.order_by('-price')
    elif sorter == 'min_price':
        phones_catalog = phones_catalog.order_by('price')

    context = {'phones': phones_catalog}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug).first()
    context = {'phone': phone}
    return render(request, template, context)
