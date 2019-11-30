# Register your models here.
from django.contrib import admin

from app.models import Product, Sale

admin.site.register(Product)
admin.site.register(Sale)
