from django.http import HttpResponse
from django.shortcuts import redirect 

def unthenticated_user(view_fun):
    def wrapper_func(request, *args , **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else : 
            return view_fun(request, *args, **kwargs)
    return wrapper_func     