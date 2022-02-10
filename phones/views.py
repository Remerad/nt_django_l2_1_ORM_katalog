from django.http import HttpResponse
from django.shortcuts import render

from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'

    phones = Phone.objects.all().order_by('release_date')
    print(phones)
    sort = request.GET.get("sort", "")
    if sort == 'name':
        phones = Phone.objects.order_by('name')
    elif sort == 'max_price':
        phones = Phone.objects.order_by('-price')
    elif sort == 'min_price':
        phones = Phone.objects.order_by('price')

    context = {
        'catalog': phones,
         }
    #return HttpResponse(phones)
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    phone = Phone.objects.filter(slug=slug)
    context = {
        'phone': phone,
    }
    return render(request, template, context)