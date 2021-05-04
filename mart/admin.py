from django.contrib import admin
from .models import Category, Product

admin.site.register(Category)


# @admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'who_for')

