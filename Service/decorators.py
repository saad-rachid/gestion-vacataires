from django.http import HttpResponse
from django.shortcuts import redirect 
from Vacataire.models import Vacataire



def allowed_user(allowed =[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):            
            group = None 
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('you are not allowed ....')
        return wrapper_func
    return decorator 



