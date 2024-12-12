"""
URL configuration for Bayer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views

Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BayerMain import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('Registration', views.Registration, name='Registration'),
    path('Login', views.LoginUser.as_view(), name='Login'),
    path('Home', views.Home, name='Home'),
    path('', views.authen, name='authenticate'),
    path('profile', views.profile, name='profile'),
    path('change_logo', views.changeLogo, name='change_logo'),
    path('Passwrd', views.passwdchange.as_view(), name='passwdchange'),
    path('category/<int:category_id>/', views.product_list, name='products'),
    path('plus_card/<int:product_id>', views.plus_card, name='plus_card'),
    path('minus_card/<int:product_id>', views.minus_cart, name='minus_card'),
    path('delete_card/<int:product_id>', views.delete_cart, name='delete_card'),
    path('add_cart/<int:product_id>', views.add_card,name='add_card'),
    path('product_info/<int:product_id>', views.product_info, name='product_info'),
    path('add_product', views.add_product, name='add_product'),
    path('add_order/', views.checkout, name='Order_check'),
    path('seller', views.sellerMain, name='seller'),
    path('orders', views.sellerOrder, name='orders'),
    path('password-reset/', views.UserForgotPasswordView.as_view(), name='password_reset'),
    path('set-new-password/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('search/', views.Search, name='search'),
]





