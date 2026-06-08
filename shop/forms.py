from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from shop.models import Category,Product

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = None

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=('name','description','stock','price','category','image')

class StockForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=('stock',)