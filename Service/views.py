from django.http import HttpResponse
from django.shortcuts import render, redirect
from  Vacataire.models import Vacataire , Absence , Seance, Assignement
from django.contrib.auth.decorators import login_required 
from .decorators import allowed_user
from accounts.models import User
from django.contrib import messages
from .forms import UploadForm
# Create your views here.


@login_required(login_url= 'login')
@allowed_user(allowed=['Employe'])
def Home(request):
    contexte = {
        'user': request.user,
        'list' : Vacataire.objects.all()
    }
    return render(request, 'index.html',contexte)


@login_required(login_url= 'login')   
@allowed_user(allowed=['Employe'])
def ManageFiliere(request):
    return render(request, 'Courses.html')

@login_required(login_url= 'login')   
@allowed_user(allowed=['Employe'])
def filiereDetails(request, name):
    form = UploadForm()
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            v = Vacataire.objects.get(user_id='i195525')
            assignement = Assignement(
            vacataire= v,
            element='Cpp',
            fichier_note=file
            )
            assignement.save()
            print(assignement)
    notes = Assignement.objects.get(element='Cpp').fichier_note
    contexte ={
        'filiere': name,
        'form': form,
        'file': notes,
    }
    return render(request, 'course-details.html', contexte)
   

@login_required(login_url= 'login')   
@allowed_user(allowed=['Employe'])
def Add(request): 
      
    if request.method == 'POST':

        cin = request.POST.get('cin')
        name = request.POST.get('name')
        email =  request.POST.get('email')
        password = request.POST.get('pass1')
        password_2 = request.POST.get('pass2')
        
        if password != password_2:
            messages.error(request,"Your passwords must match")
        else :    
            user = User.objects.create_user(email, password[0],  cin=cin, name=name)
            return redirect('create', pk=cin)
    return render(request, 'add.html')  


@login_required(login_url= 'login')   
@allowed_user(allowed=['Employe'])
def CreateProfile(request,pk):
    v = Vacataire.objects.filter(user_id = pk)
    print(v)
    if v :
        if request.method == 'POST':
           tel = request.POST.get('tel')
           dept = request.POST.get('departement')
           fonction = request.POST.get('Fonction')
           banque = request.POST.get('Banque')
           rib = request.POST.get('rib')
           nbre_heure =  request.POST.get('nbre')
           remuniration = request.POST.get('remuniration')
           expiration_date = request.POST.get('finish')

           v.update(tel=tel, expiration_date=expiration_date, dept=dept, fonction=fonction, banque=banque, rib=rib, remuniration=remuniration, nbre_heure=nbre_heure) 
           return redirect('home')        
        return render(request, 'ADD2.html')    
    else :
        return redirect('add')
    



@login_required(login_url= 'login')   
@allowed_user(allowed=['Employe'])
def Details(request, name):
    user = User.objects.get(name = name)
    print(user)
    contexte = {
        'nom' : user.get_full_name(),
        'date': user.date_created,
        'v': Vacataire.objects.get(user_id = user.cin),
    }

    return render(request, 'vacataire-details.html', contexte)



@login_required(login_url= 'login')   
@allowed_user(allowed=['Employe'])
def assign_courses(request):
    pass






