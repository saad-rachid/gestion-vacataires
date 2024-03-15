from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Service.decorators import allowed_user 
from .models import Seance, Vacataire , Absence

# Create your views here.


@login_required(login_url= 'login')
@allowed_user(allowed=['Vacataire'])
def HomeV(request):
    contexte = {
        'user': request.user,
        'list': Seance.objects.all() 
        
    }
    return render(request, 'index.html',contexte)


@login_required(login_url= 'login')
@allowed_user(allowed=['Vacataire'])
def Profile(request):
    v = Vacataire.objects.filter(user_id = request.user.cin)
    if v :
        return render(request ,'profileV.html', {'v': v} )
    else :
        return HttpResponse("profile doesn't exist....") 
  

@login_required(login_url= 'login')   
@allowed_user(allowed=['Vacataire'])
def MentionMarks(request):
    pass 


@login_required(login_url= 'login')   
@allowed_user(allowed=['Vacataire'])
def ManageAbsence(request):

    seances = Seance.objects.filter(vacataire_id = request.user.cin)
    list = [list.append(Absence.objects.filter(seance_id = s.code)) for s in seances]
    
    contexte = {
        'v' : Vacataire.objects.filter(user_id = request.user.cin),
        'list' : list,

    }
    
    return render(request, 'Absences.html', contexte)


@login_required(login_url= 'login')   
@allowed_user(allowed=['Vacataire'])
def Justify(request, pk):
    abs = Absence.objects.get()



