from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.contrib.messages.views import SuccessMessageMixin

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView

from BayerMain.models import Role, Product, Category, Cart, CartItem, Feedback, Order, OrderItem, Sales, productSales, imageUser, location
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import UserForm, LoginForm, addProductForm, add_Feedback, Order_check, changeLogoForm, UserForgotPasswordForm, UserSetNewPasswordForm


def Registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user1 = form.save(commit=False)
            user1.username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            password = user1.set_password(form.cleaned_data['password'])
            email = form.cleaned_data.get('email')
            form.save()
            user_role = Role.objects.create(user=user1, role=form.cleaned_data['Role'])
            user = authenticate(username=first_name, password=password, email=email, role=user_role, first_name=first_name, last_name=last_name)

            return redirect('Login')
    else:
        form = UserForm()
    return render(request, 'Registration.html', context={'form': form})







class LoginUser(LoginView):
    template_name = 'Login.html'
    form_class = LoginForm
    extra_context = {'title': 'Login'}

    def get_success_url(self):
        userrole = Role.objects.get(user=self.request.user).role
        if userrole == "customer":
            return reverse_lazy('Home')
        elif userrole == "seller":
            return reverse_lazy('seller')



def authen(request):
    return render(request, 'authorization.html')








class UserForgotPasswordView(SuccessMessageMixin, PasswordResetView):
    """
    Представление по сбросу пароля по почте
    """
    form_class = UserForgotPasswordForm
    template_name = 'changepasswd.html'
    success_url = reverse_lazy('home')
    success_message = 'Письмо с инструкцией по восстановлению пароля отправлена на ваш email'
    subject_template_name = 'system/email/password_subject_reset_mail.txt'
    email_template_name = 'system/email/password_reset_mail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Запрос на восстановление пароля'
        return context


class UserPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    """
    Представление установки нового пароля
    """
    form_class = UserSetNewPasswordForm
    template_name = 'changepasswddone.html'
    success_url = reverse_lazy('home')
    success_message = 'Пароль успешно изменен. Можете авторизоваться на сайте.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Установить новый пароль'
        return context








def profile(request):
    user = request.user
    img = imageUser.objects.get(user=user)
    Orderuser = Order.objects.filter(user=user)

    user_profile = imageUser.objects.get(user=request.user)
    if request.method == 'POST':
        form = changeLogoForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = changeLogoForm(instance=user_profile)

    return render(request, 'profile.html', context={'img': img, 'user': user, 'Orderuser': Orderuser,'form':form})


def changeLogo(request):
    user_profile = imageUser.objects.get(user=request.user)
    if request.method == 'POST':
        form = changeLogoForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = changeLogoForm(instance=user_profile)
    return render(request, 'baseIndex.html', {'form': form})





class passwdchange(PasswordChangeView):
    form = PasswordChangeForm
    success_url = reverse_lazy('#')
    template_name = 'PasswdChange.html'



def Home(request):
    user = request.user

    if user.is_anonymous:
        categories = Category.objects.all()
        return render(request, 'index.html', {'categories': categories})
    else:
        cart = Cart.objects.get_or_create(user=user, status='open')
        images = imageUser.objects.get_or_create(user=user)
        locations = location.objects.get_or_create(user=user)
        categories = Category.objects.all()
        cartUser = Cart.objects.get(user=user, status='open')
        cartItems = CartItem.objects.filter(cart=cartUser).all()
        products = Product.objects.all()
        sales = Sales.objects.all()
        productsales = productSales.objects.all()
        logo = imageUser.objects.get(user=user)

    return render(request, 'indexClient.html', {'categories': categories, 'error': get_object_or_404, 'user': user, 'cartItems': cartItems, 'cartUser': cartUser, 'products': products, 'sales': sales, 'productsales': productsales, 'logo': logo})




def Search(request):
    logo = imageUser.objects.get(user=request.user)
    query = request.GET.get('q', '')
    results = []
    if query:
        results = Product.objects.filter(name__icontains=query)
    else:
        results = Product.objects.all()
    return render(request, 'search.html', {'results': results, 'query': query, 'logo': logo})






def product_list(request, category_id):
    user = request.user
    logo = imageUser.objects.get(user=user)
    cart_user = Cart.objects.get(user=user, status='open')
    cart_items = CartItem.objects.filter(cart=cart_user).all()
    cartUser = Cart.objects.get(user=user, status='open')
    if request.method == 'POST':
        products = Product
        cart = Cart.objects.get(user=request.user, status='open')
        cart_item = CartItem.objects.create(cart=cart, product_id=products, quantity=1)

    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)



    return render(request, 'products.html', {'products': products, 'category': category, 'cartItems': cart_items, 'cartUser': cartUser, 'user': user, 'logo': logo})





def add_card(request, product_id):
    product = get_object_or_404(Product.objects.all(), id=product_id)
    cart = Cart.objects.get(user=request.user, status='open')
    cart_item = CartItem.objects.filter(cart=cart, product=product)

    if not cart_item:
        CartItem.objects.create(cart=cart, product=product, quantity=1, sumtotal=product.price)
        if cart.total_price == 0:
            cart.total_price = product.price
            cart.save()
        elif cart.total_price >= 0:
            cart.total_price += product.price
            cart.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        cart_item = cart_item.first()
        cart_item.quantity += 1
        cart_item.sumtotal += cart_item.product.price
        cart.total_price += cart_item.product.price
        cart.save()
        cart_item.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




def plus_card(request, product_id):
    product = get_object_or_404(Product.objects.all(), id=product_id)
    cart = Cart.objects.get(user=request.user, status='open')
    cart_item = CartItem.objects.filter(cart=cart, product=product)

    if not cart_item:
        CartItem.objects.create(cart=cart, product=product, quantity=1, sumtotal=product.price)
        if cart.total_price == 0:
            cart.total_price = product.price
            cart.save()
        elif cart.total_price >= 0:
            cart.total_price += product.price
            cart.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        cart_item = cart_item.first()
        cart_item.quantity += 1
        cart_item.sumtotal += cart_item.product.price
        cart.total_price += cart_item.product.price
        cart.save()
        cart_item.save()

        cartUser = Cart.objects.get(user=request.user, status='open')
        cartItems = CartItem.objects.filter(cart=cartUser).all()
        return render(request, 'cart_products.html', {'cartItems': cartItems, 'cartUser': cartUser, 'product': product})


def minus_cart(request, product_id):
    product = get_object_or_404(Product.objects.all(), id=product_id)
    cart = Cart.objects.get(user=request.user, status='open')
    cart_item = CartItem.objects.filter(cart=cart, product=product)
    cart_item = cart_item.first()

    if cart_item.quantity >= 1:
        cart_item.quantity -= 1
        cart_item.sumtotal -= cart_item.product.price
        cart.total_price -= cart_item.product.price
        cart.save()
        cart_item.save()
    elif cart_item.quantity <= 0:
        cart.total_price = 0


    cartUser = Cart.objects.get(user=request.user, status='open')
    cartItems = CartItem.objects.filter(cart=cartUser).all()
    return render(request, 'cart_products.html', {'cartItems': cartItems, 'cartUser': cartUser, 'product': product})



def delete_cart(request, product_id):
    product = get_object_or_404(Product.objects.all(), id=product_id)
    cart = Cart.objects.get(user=request.user, status='open')
    cart_item = CartItem.objects.filter(cart=cart, product=product)
    cart_item = cart_item.first()
    cart.total_price -= cart_item.sumtotal
    cart.save()
    cart_item.delete()

    cartUser = Cart.objects.get(user=request.user, status='open')
    cartItems = CartItem.objects.filter(cart=cartUser).all()
    return render(request, 'cart_products.html', {'cartItems': cartItems, 'cartUser': cartUser, 'product': product})


def product_info(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cartUser = Cart.objects.get(user=request.user, status='open')
    cartItems = CartItem.objects.filter(cart=cartUser).all()
    messages = Feedback.objects.filter(product=product).all()

    if request.method == 'POST':
        form = add_Feedback(request.POST)
        if form.is_valid():
            form_message = form.save(commit=False)
            form_message.product = product
            form_message.client = request.user
            form_message.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = add_Feedback()
        return render(request, 'product_info.html', {'product': product, 'cartUser': cartUser, 'cartItems': cartItems, 'form': form, 'messages': messages})




def add_product(request):
    if request.method == 'POST':
        form = addProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('seller')
    else:
        form = addProductForm()
        return render(request, 'seller/add_product.html', context={'form': form})




def checkout(request):
    user = request.user
    cart = Cart.objects.get(user=request.user, status='open')
    cart_Item = CartItem.objects.filter(cart=cart).all()
    locations = location.objects.get(user=user).location


    if request.method == 'POST':
        form = Order_check(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = cart.total_price
            order.location = locations
            order.cart = cart
            cart.status = 'close'
            cart.save()
            order.save()
            for item in cart_Item:
                OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity, seller=item.product.seller)
            return redirect('Home')

    else:
        form = Order_check()

        return render(request, 'CheckOut.html', context={'cart': cart, 'cart_Item': cart_Item, 'user': user, 'form': form})



def sellerMain(request):
    user = request.user
    logo = imageUser.objects.get(user=user)
    categories = Category.objects.all()
    order_items = OrderItem.objects.filter(seller=user).all()
    products_by_category = {}

    for category in categories:
        products = Product.objects.filter(seller=user, category=category)
        if products.exists():
            products_by_category[category] = products

    return render(request, 'Seller/SellerBase.html', context={'user': user, 'categories': categories, 'products_by_category': products_by_category, 'logo':logo,'order_items': order_items})


def sellerOrder(request):
    user = request.user
    order_items = OrderItem.objects.filter(seller=user).all()
    return render(request, 'Seller/SellerBase.html', context={'user': user, 'order_items': order_items})
