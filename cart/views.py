from django.shortcuts import render,redirect
from django.views import View
from shop.models import Product
from cart.models import Cart
from cart.forms import OrderForm
import razorpay
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from cart.models import Order,OrderItems
import uuid

class AddToCart(View):
    def get(self, request, i):
        u=request.user
        p=Product.objects.get(id=i)
        try:
            c=Cart.objects.get(user=u,product=p)

            # prevent adding more than stock
            if p.stock > 0:
                c.quantity += 1
                c.save()

        except:
            c=Cart.objects.create(user=u,product=p,quantity=1)
            c.save()

        # Reduce stock
        p.stock -= 1
        p.save()

        return redirect('cart:cartview')

class CartView(View):
    def get(self, request):
        u=request.user
        total=0
        price=0
        c=Cart.objects.filter(user=u)
        for i in c:
            total += i.subtotal()
            price=(total)+40-10
        context={'cart': c, 'subtotal': total, 'price': price}
        return render(request, 'cart.html', context)
    
class CartRemove(View):
    def get(self, request, i):
        c=Cart.objects.get(id=i)

        # return stock
        p=c.product
        p.stock += 1
        p.save()

        try:
            if c.quantity>1:
                c.quantity -= 1
                c.save()
            else:
                c.delete()
        except:
            pass
        return redirect('cart:cartview')
    
class CartDelete(View):
    def get(self, request, i):
        try:
            c=Cart.objects.get(id=i)

            # restore stock
            p=c.product
            p.stock += c.quantity
            p.save()
            
            c.delete()
        except:
            pass
        return redirect('cart:cartview')
    
class CheckOut(View):
    def get(self, request):
        form_instance=OrderForm()
        context={'form': form_instance}
        return render(request, 'checkout.html', context)
    
    def post(self, request):
        form_instance=OrderForm(request.POST)
        if form_instance.is_valid():
            f=form_instance.save(commit=False)
            # User
            u=request.user
            f.user=u
            # Order amount
            c=Cart.objects.filter(user=u)
            total=0
            for i in c:
                total += i.subtotal()
                price=(total)+40-10
            f.order_amount=price
            f.save()

            # Online Payment
            if f.payment_method=="Online":
                
                # create a razorpay client connection using keys
                client=razorpay.Client(auth=('REMOVED_RAZORPAY_KEY_ID','REMOVED_RAZORPAY_SECRET'))

                # create a new order in razorpay
                response_payment = client.order.create({
                    "amount": int(f.order_amount*100),
                    "currency": "INR",
                    "payment_capture": "1"
                    })
                print(response_payment)

                # retrieve the order id from response payment
                id=response_payment['id']
                # adds to the order record stored in our db table
                f.order_id=id
                f.save()
                context={'payment':response_payment, 'order':f}
                return render(request, 'payment.html', context)
            # Cash on Delivery
            else:
                cid=uuid.uuid4().hex[:8]
                di='order_cod'+cid
                f.order_id=di
                f.is_ordered=True
                f.save()

                c=Cart.objects.filter(user=u)
                for i in c:
                    item=OrderItems.objects.create(product=i.product,order=f,quantity=i.quantity)
                    item.save()
                c.delete()
                return render(request, 'payment.html')

@method_decorator(csrf_exempt, name='dispatch')
class PaymentSuccess(View):
    def post(self, request):
        response=request.POST
        print(response)

        # After successful payment mark is_ordered as True
        id=response['razorpay_order_id']
        c=Order.objects.get(order_id=id)
        c.is_ordered=True
        c.save()

        # Fetch the cart items selected by user
        o=Cart.objects.filter(user=c.user)
        for i in o:
            a=OrderItems.objects.create(product=i.product,order=c,quantity=i.quantity)
            a.save()
        o.delete()
        return render(request, 'payment_success.html')

class MyOrder(View):
    def get(self, request):
        u=request.user
        o=Order.objects.filter(user=u,is_ordered=True)
        context={'orders':o}
        return render(request, 'my_order.html', context)