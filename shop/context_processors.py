from shop.models import Category

def dropdown_menu(request):
    c=Category.objects.all()
    return {'dropdown': c}