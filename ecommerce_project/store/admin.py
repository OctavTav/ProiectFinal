from django.contrib import admin
from .models import Category, Product


# Register your models here.

class ProductAdmin(admin.ModelAdmin):  # use this to view more info about in the admin page regarding products
    list_display = ['name', 'price', 'stock', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20


class CategoryAdmin(admin.ModelAdmin):  # same as above but for categories
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin,)
