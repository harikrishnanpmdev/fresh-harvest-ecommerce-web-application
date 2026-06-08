from django.shortcuts import render
from django.views import View
from shop.models import Product
from django.db.models import Q

class SearchView(View):
    def get(self,request):
        srh=request.GET['p']
        b=Product.objects.filter(Q(name__icontains=srh) |
                                  Q(price__icontains=srh))
        context={'products': b}
        return render(request, 'search.html', context)