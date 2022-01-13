from basketapp.models import BasketItem


def get_basket(request):
    basket = []

    if request.user.is_authenticated:
        basket = BasketItem.objects.filter(user=request.user)

    return {'basket': basket}