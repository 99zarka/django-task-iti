from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'product_quantity', 'order_date')
    list_filter = ('order_date', 'user', 'product')
    search_fields = ('user__username', 'product__name', 'address', 'email')
    raw_id_fields = ('product',) # Use a raw ID field for product selection
