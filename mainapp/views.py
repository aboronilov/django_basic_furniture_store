import random

from django.core.cache import cache
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page

from mainapp.models import Product, ProductCategory


@cache_page(60*15)
def get_menu():
    return ProductCategory.objects.all()



def get_hot_product():
    product_ids = Product.objects.values_list('id', flat=True).all()
    random_id = random.choice(product_ids)
    return Product.objects.get(pk=random_id)


@cache_page(60*15)
def same_products(hot_product):
    similar = cache.get('similar')
    if not similar:
        similar = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
        cache.set('similar', similar, 60*15)
    return similar


def index(request):
    context = {
        'page_title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)



def products(request):
    hot_product = get_hot_product()
    context = {
        'page_title': 'каталог',
        'hot_product': hot_product,
        'same_products': same_products(hot_product),
        'categories': get_menu(),
    }
    return render(request, 'mainapp/products.html', context)



def category(request, pk):
    page_num = request.GET.get('page', 1)
    if pk == 0:
        category = {'pk': 0, 'name': 'все'}
        products = Product.objects.all()
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = category.product_set.all()

    products_paginator = Paginator(products, 2)
    try:
        products = products_paginator.page(page_num)
    except PageNotAnInteger:
        products = products_paginator.page(1)
    except EmptyPage:
        products = products_paginator.page(products_paginator.num_pages)

    context = {
        'page_title': 'товары категории',
        'categories': get_menu(),
        'category': category,
        'products': products,
    }
    return render(request, 'mainapp/category_products.html', context)


@cache_page(60*15)
def product_page(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'page_title': 'страница продукта',
        'product': product,
        'categories': get_menu(),
    }
    return render(request, 'mainapp/product_page.html', context)


@cache_page(60*15)
def contact(request):
    locations = [
        {'city': 'Москва',
         'phone': '+7-888-444-7777',
         'email': 'info@geekshop.ru',
         'address': 'В пределах МКАД'},
        {'city': 'Санкт-Петербург',
         'phone': '+7-888-333-9999',
         'email': 'info.spb@geekshop.ru',
         'address': 'В пределах КАД'},
        {'city': 'Хабаровск',
         'phone': '+7-888-222-3333',
         'email': 'info.east@geekshop.ru',
         'address': 'В пределах центра'},
    ]

    context = {
        'page_title': 'контакты',
        'locations': locations,
    }
    return render(request, 'mainapp/contact.html', context)
