from  django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm, DateTimeInput
from .models import Role, Product, Category, Feedback,Order, imageUser


class UserForm(ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name','class': 'Last name'}))
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'username', 'name': 'Username','class':'username'}))
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={'placeholder': 'Email Address', 'class': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password', 'name': 'Password'}))
    Role = forms.ChoiceField(choices=Role.ROLE_CHOICES, widget=forms.RadioSelect(), label='Role')


    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', 'Role', 'first_name', 'last_name')


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')

    error_messages = {
        'invalid_login': 'Пожалуйста введите правильный пароль или логин'
    }




class changeLogoForm(forms.ModelForm):

    class Meta:
        model = imageUser
        fields = ('image',)
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control form-control-sm', 'id':'formFileLg'}),
        }




class addProductForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
        'id': 'category-selector'
    }),
    empty_label="Выберите категорию")
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'category', 'image')


class add_Feedback(ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control h-25'}))
    class Meta:
        model = Feedback
        fields = ('message',)


class Order_check(ModelForm):
    payment_method = forms.ChoiceField(choices=Order.METHOD_CHOICES, widget=forms.RadioSelect(attrs={'class': 'btn btn-check', 'id': 'pk',type:'button'}))
    method_obtaining = forms.ChoiceField(choices=Order.METHOD_OBTAINING_CHOICES, widget=forms.RadioSelect(attrs={'class': 'btn btn-check samovyzov', 'id': 'hh pk',type:'button'}))
    location = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Order
        fields = ('payment_method', 'method_obtaining', 'location')



from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


class UserForgotPasswordForm(PasswordResetForm):
    """
    Запрос на восстановление пароля
    """

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })


class UserSetNewPasswordForm(SetPasswordForm):
    """
    Изменение пароля пользователя после подтверждения
    """

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })


