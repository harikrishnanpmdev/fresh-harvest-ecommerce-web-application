from django.http import HttpResponse

def admin_required(fun):
    def wrapper(request):
        if not request.user.is_superuser:
            return HttpResponse("Access Denied")
        else:
            return fun(request)
    return wrapper

def user_required(fun):
    def wrapper(request):
        if request.user.is_superuser:
            return HttpResponse("Access Denied")
        else:
            return fun(request)
    return wrapper