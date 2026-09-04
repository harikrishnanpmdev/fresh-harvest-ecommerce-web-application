from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.utils.decorators import method_decorator
from django.views import View
from shop.forms import RegisterForm,LoginForm,CategoryForm,ProductForm,StockForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from shop.models import Category,Product
from shop.decorators import admin_required, user_required

class Categories(View):
    def get(self, request):
        c=Category.objects.all()
        context={'categories': c}
        return render(request, 'categories.html', context)
    
class Products(View):
    def get(self, request,i):
        p=Category.objects.get(id=i)
        context={'products': p}
        return render(request, 'products.html', context)

@method_decorator(admin_required, name='dispatch')
@method_decorator(login_required, name='dispatch')
class Adminhome(View):
    def get(self, request):
        return render(request, 'adminhome.html')

@method_decorator(user_required, name='dispatch')
@method_decorator(login_required, name='dispatch')
class Userhome(View):
    def get(self, request):
        return render(request, 'userhome.html')
    
class Register(View):
    def get(self, request):
        form_instance= RegisterForm()
        context={'form': form_instance}
        return render(request, 'register.html', context)
    
    def post(self, request):
        form_instance= RegisterForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
        return redirect('shop:login')
        
class Login(View):
    def get(self, request):
        form_instance= LoginForm()
        context={'form': form_instance}
        return render(request, 'login.html', context)
    
    def post(self, request):
        form_instance= LoginForm(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            u=data['username']
            p=data['password']
            user=authenticate(username=u,password=p)
            if user and user.is_superuser == True:
                login(request, user)
                return redirect('shop:adminhome')
            elif user and user.is_superuser == False:
                login(request, user)
                return redirect('shop:userhome')
            else:
                messages.error(request, "Invalid User Credentials")
                return redirect('shop:login')
            
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('shop:login')

@method_decorator(admin_required, name='dispatch')
@method_decorator(login_required, name='dispatch')
class AddCategory(View):
    def get(self, request):
        form_instance= CategoryForm()
        context={'form': form_instance}
        return render(request, 'addcategory.html', context)
    
    def post(self, request):
        form_instance= CategoryForm(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('shop:categories')

@method_decorator(admin_required, name='dispatch')
@method_decorator(login_required, name='dispatch')
class AddProduct(View):
    def get(self, request):
        form_instance= ProductForm()
        context={'form': form_instance}
        return render(request, 'addproduct.html', context)
    
    def post(self, request):
        form_instance= ProductForm(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('shop:categories')
        
class ProductDetail(View):
    def get(self, request, i):
        p=Product.objects.get(id=i)
        context={'product': p}
        return render(request, 'productdetail.html', context)

@method_decorator(admin_required, name='dispatch')
@method_decorator(login_required, name='dispatch')
class AddStock(View):
    def get(self, request, i):
        p=Product.objects.get(id=i)
        form_instance= StockForm(instance=p)
        context={'form': form_instance}
        return render(request, 'addstock.html', context)
    
    def post(self, request, i):
        p=Product.objects.get(id=i)
        form_instance= StockForm(request.POST, instance=p)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('shop:categories')