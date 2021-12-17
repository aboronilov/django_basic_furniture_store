# import pickle
#
# from django.core.management.base import BaseCommand
#
# from authapp.models import ShopUser
# from mainapp.models import Product, ProductCategory
#
#
# def write_to_pickle(data, file_name):
#     with open(file_name, 'wb') as infile:
#         return pickle.dump(data, infile)
#
#
# class Command(BaseCommand):
#     help = 'Dump data from db'
#
#     def handle(self, *args, **options):
#         schema = ('name', 'description', 'short_desc')
#         items = []
#         for item in ProductCategory.objects.all():
#             items.append({key: val
#                           for key, val in vars(item).items()
#                           if key in schema})
#
#         items = write_to_pickle('mainapp/json/products.json')
#         for item in items:
#             category = ProductCategory.objects.get(name=item['category'])
#             item['category'] = category
#             Product.objects.create(**item)
#
#         if not ShopUser.objects.filter(username='django').exists():
#             ShopUser.objects.create_superuser('django', 'django@gb.local', 'geekbrains')
