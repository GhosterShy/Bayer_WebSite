from django.contrib import admin
# admin.py
from django.contrib import admin
from .models import Role, Product, Cart, CartItem, Order, OrderItem, Delivery,Category,Feedback

# Регистрируем модель ролей
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_filter = ('role',)
    search_fields = ('user__username',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)



# Регистрируем модель продукта
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'seller', 'category')
    search_fields = ('name', 'description', 'seller__username')
    list_filter = ('category', 'seller__username')



@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('product', 'client', 'message')
    search_fields = ('product', 'client')
    list_filter = ('product', 'client__username')



@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price', 'status', 'payment_method')
    list_filter = ('status', 'payment_method')
    search_fields = ('user__username',)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')
    search_fields = ('cart__user__username', 'product__name')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price', 'status', 'payment_method', 'created_at')
    list_filter = ('status', 'payment_method')
    search_fields = ('user__username', 'cart__id')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity')
    search_fields = ('order__user__username', 'product__name')


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('order', 'delivery_service', 'status', 'delivery_date')
    list_filter = ('status', 'delivery_service')
    search_fields = ('order__user__username', 'delivery_service')


# Register your models here.
