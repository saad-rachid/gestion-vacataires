from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from  .decorators  import unthenticated_user
# Create your views here.


@unthenticated_user
def Login(request):
    username = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')





def Logout(request):
    logout(request)
    return redirect('login')
