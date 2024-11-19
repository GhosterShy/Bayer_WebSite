from django.db import models
from django.contrib.auth.models import User

# Модель для Пользователя
class Role(models.Model):
    ROLE_CHOICES = (
        ('customer', 'Клиент'),
        ('seller', 'Продавец'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)



class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='static/img/categoryis', null=True)
    title = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=250000, null=True)
    image_link1 = models.ImageField(upload_to='static/img/categoryis', null=True)
    image_link2 = models.ImageField(upload_to='static/img/categoryis', null=True)

    def __str__(self):
        return self.name



# Модель для Продукта
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True)
    image = models.ImageField(upload_to='static/images', null=True, blank=True)

    def __str__(self):
        return self.name




class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client')
    message = models.TextField(max_length=250, null=True)


# Модель для Корзины
class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    status = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    sumtotal = models.IntegerField(default=0.0)

# Модель для Заказа
class Order(models.Model):
    METHOD_CHOICES = (
        ('kaspi', 'Kaspi'),
        ('card', 'Картой при получений'),
        ('cash', 'Наличными при получений'),
    )
    METHOD_OBTAINING_CHOICES = (
        ('delivery', 'Доставка'),
        ('selfcoll', 'Cамовызов'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='Open')
    payment_method = models.CharField(max_length=50, choices= METHOD_CHOICES)
    method_obtaining = models.CharField(max_length=50, choices=METHOD_OBTAINING_CHOICES, default='selfcoll')
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

# Модель для Доставки
class Delivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    delivery_service = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    delivery_date = models.DateTimeField(null=True, blank=True)




