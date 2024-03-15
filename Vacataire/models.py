from django.db import models
#from accounts.models import Vacataire

# Create your models here.



class Vacataire(models.Model):
    
    ING = 'ingenieur'
    INGENIEUR_EN_CHEF = 'Ing en chef '
    PROF_ASSISTANT = 'prof assistant '
    PROF_ABILITE = 'PROF_ABILITE'
    DOCTORANT = 'DOCTORANT'
    PES =  'PES'
    PROF_AGREGE = 'PROF AGREGE'


    fonctions= [
        (ING, 'INGENIEUR'),
        (INGENIEUR_EN_CHEF, 'INGENIEUR EN CHEF '),
        (PROF_ASSISTANT , 'PROF ASSISTANT'),
        (PROF_ABILITE , 'PROF_ABILITE'),
        (DOCTORANT , 'DOCTORANT'),
        (PES , 'PES'),
        (PROF_AGREGE , 'PROF AGREGE')

    ]

   

    user = models.OneToOneField("accounts.User", on_delete=models.CASCADE, primary_key=True)
    tel = models.CharField(max_length=15, null = True)
    expiration_date = models.DateTimeField(auto_now=False, auto_now_add=False, null =True)
    dept = models.CharField(max_length= 30, null = True)
    fonction = models.CharField(max_length=50 , choices= fonctions , null = True)
    banque = models.CharField(max_length=50, null = True)
    rib = models.CharField(max_length=50 , null = True)
    remuniration = models.DecimalField(max_digits=10, decimal_places=2, null = True)
    nbre_heure = models.IntegerField(null = True)
    img = models.ImageField(null = True, blank = True)

    def update(self, tel , expiration_date, dept, fonction, banque, rib, remuniration, nbre_heure):
        self.tel = tel
        self.expiration_date = expiration_date
        self.dept = dept 
        self.fonction = fonction 
        self.banque = banque
        self.rib = rib 
        self.remuniration = remuniration
        self.nbre_heure = nbre_heure


class Assignement(models.Model):
    vacataire = models.ForeignKey("Vacataire.Vacataire",on_delete=models.CASCADE, related_name='assignements')
    filiere = models.CharField(max_length=10, null=True)
    promotion = models.IntegerField(null=True)
    element =  models.CharField(max_length=50, primary_key=True)
    fichier_note = models.FileField(null =True)


class Seance(models.Model):

    types = (
        ('TP', 'TP'),
        ('COURS', 'COURS'),
        ('TD','TD'),
        ('CC','CC'),

    )

    Assignement = models.ForeignKey("Vacataire.Assignement", on_delete=models.CASCADE)
    jour = models.CharField( max_length=15)
    horaire = models.TimeField()
    date_seance = models.DateField()
    type = models.CharField(max_length=50, choices = types )
    salle = models.CharField(max_length=10)
    

class Presence(models.Model):
    vacataire = models.ForeignKey("Vacataire.Vacataire", null = True , on_delete=models.SET_NULL, related_name="activite")
    seance = models.ForeignKey("Vacataire.Seance", null = True ,on_delete=models.SET_NULL)
    horraire = models.DateTimeField(auto_now_add=True)
    present = models.BooleanField(default= False)

class Absence(models.Model):
    vacataire = models.ForeignKey("Vacataire.Vacataire",  on_delete=models.CASCADE)  
    seance = models.OneToOneField("Vacataire.Seance", null= True ,on_delete=models.SET_NULL)
    justifiee = models.BooleanField(default=False) 
    motif = models.CharField(max_length=50, default= 'malade')
    justif= models.FileField(upload_to=None, max_length=100, null=True)

