from django.shortcuts import render

import json
import os

from mainapp.models import Product,ProductCategory

MODULE_DIR =os.path.dirname(__file__)
# Create your views here.

def index(request):
    context = {
        'title': 'Geekshop', }
    return render(request, 'mainapp/index.html', context)


def products(request):
    # file_path = os.path.join(MODULE_DIR,'fixtures/goods.json')
    context = {
        'title': 'Geekshop | Каталог',
    }

    # context['products'] = json.load(open(file_path,encoding='utf-8'))
    context['products'] = Product.objects.all()
    context['categories'] = ProductCategory.objects.all()
    return render(request, 'mainapp/products.html', context)
