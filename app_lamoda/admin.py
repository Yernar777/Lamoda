from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(LamodaCategory)
admin.site.register(LamodaShapka)
admin.site.register(LamodaShapka1)
admin.site.register(Review1)
admin.site.register(Cart)
admin.site.register(CartItem)



class OrderItemInline(admin.TabularInline):
    model = OrderItem
    can_delete = False
    readonly_fields = ['product', 'product_price', 'quantity']
    extra = 0
    fields = ['product', 'product_price', 'quantity']

    def product_price(self, obj):
        return obj.product.price

    product_price.short_description = 'Цена за единицу'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'total_price', 'created_at']
    search_fields = ['name', 'phone']
    inlines = [OrderItemInline]