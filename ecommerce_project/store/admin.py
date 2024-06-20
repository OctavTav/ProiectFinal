from django.contrib import admin
from .models import Category, Product, Order, OrderItem


# Register your models here.

class ProductAdmin(admin.ModelAdmin):  # use this to view more info about in the admin page regarding products
    list_display = ['name', 'price', 'stock', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20


class CategoryAdmin(admin.ModelAdmin):  # same as above but for categories
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class OrderItemAdmin(admin.TabularInline):  # class inherited is for better view
    model=OrderItem
    fieldsets=[
        ('Product', {'fields': ['product'], }),
        ('Quantity', {'fields': ['quantity'], }),
        ('Price', {'fields': ['price'], }),
    ]
    readonly_fields = ['product', 'quantity', 'price']
    can_delete = False # so that the product can't be deleted from a completed order
    max_num = 0


# decorator build-in to check if admin is logged
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'billingName', 'emailAddress', 'created']
    list_display_links = ('id', 'billingName')
    search_fields = ['id', 'billingName', 'emailAddress']
    readonly_fields = ['id', 'token', 'total', 'emailAddress', 'created',
                       'billingName', 'billingAddress1', 'billingCity', 'billingPostcode',
                       'billingCountry', 'shippingName', 'shippingAddress1', 'shippingCity',
                       'shippingPostcode', 'shippingCountry']

    fieldsets = [
        ('ORDER INFORMATION', {'fields': ['id', 'token', 'total', 'created']}),
        ('BILLING INFORMATION', {'fields': ['billingName', 'billingAddress1',
                                            'billingCity', 'billingPostcode', 'billingCountry', 'emailAddress']}),
        ('SHIPPING INFORMATION', {'fields': ['shippingName', 'shippingAddress1',
                                             'shippingCity', 'shippingPostcode', 'shippingCountry']}),
    ]

    inlines = [
        OrderItemAdmin,
    ]

    # the 2 functions below make sure that admin cannot delete or add orders on it's own
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin,)
