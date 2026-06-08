from django.urls import path
from cart import views
app_name="cart"

urlpatterns = [
    path('addtocart/<int:i>', views.AddToCart.as_view(), name='addtocart'),
    path('cartview', views.CartView.as_view(), name='cartview'),
    path('cartremove/<int:i>', views.CartRemove.as_view(), name='cartremove'),
    path('cartdelete/<int:i>', views.CartDelete.as_view(), name='cartdelete'),
    path('checkout', views.CheckOut.as_view(), name='checkout'),
    path('success', views.PaymentSuccess.as_view(), name='success'),
    path('myorder', views.MyOrder.as_view(), name='myorder'),
]