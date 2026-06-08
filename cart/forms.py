from django import forms
from cart.models import Order

class OrderForm(forms.ModelForm):

    payment_choice=[("Cash","Cash on Delivery"),("Online","Online Payment")]
    payment_method=forms.ChoiceField(choices=payment_choice)

    class Meta:
        model=Order
        fields=('address','phone','payment_method')