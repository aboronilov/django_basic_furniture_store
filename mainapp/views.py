from django.shortcuts import render

from mainapp.models import Product, ProductCategory


def index(request):
    context = {
        'page_title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    product_1 = Product.objects.all()[0]
    menu = {'goods': 'все',
            'home': 'дом',
            'office': 'офис',
            'modern': 'модерн',
            'classic': 'классика'}

    categories = ProductCategory.objects.all()

    context = {
        'page_title': 'каталог',
        'product_1': product_1,
        'categories': categories
    }

    return render(request, 'mainapp/products.html', context)


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


def category(request, pk):
    pass
