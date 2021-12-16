from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.

# 1:25
from basketapp.models import BasketItem


def index(request):
    pass
    # basket = request.user.basket.get_or_create()


def add(request, product_pk):
    basket_item, _ = BasketItem.objects.get_or_create(
        user=request.user,
        product_id=product_pk
    )
    basket_item.qty += 1
    basket_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove(request, pk):
    pass
