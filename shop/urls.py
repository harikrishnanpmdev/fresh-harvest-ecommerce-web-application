from django.urls import path
from shop import views
app_name="shop"

urlpatterns = [
    path('', views.Categories.as_view(), name='categories'),
    path('register', views.Register.as_view(), name= 'register'),
    path('login', views.Login.as_view(), name= 'login'),
    path('logout', views.Logout.as_view(), name= 'logout'),
    path('adminhome', views.Adminhome.as_view(), name= 'adminhome'),
    path('userhome', views.Userhome.as_view(), name= 'userhome'),
    path('products/<int:i>', views.Products.as_view(), name= 'products'),
    path('addcategory', views.AddCategory.as_view(), name= 'addcategory'),
    path('addproduct', views.AddProduct.as_view(), name= 'addproduct'),
    path('productdetail/<int:i>', views.ProductDetail.as_view(), name= 'productdetail'),
    path('addstock/<int:i>', views.AddStock.as_view(), name= 'addstock'),
]