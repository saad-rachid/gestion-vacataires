from accounts.models import User 
from Vacataire.models import Vacataire
from django.db.models .signals import post_save
from django.dispatch import receiver 
from django.contrib.auth.models import Group








@receiver(post_save, sender= User)
def create_profileV(sender, instance, created , **kwargs ):
    groups = instance.groups.all()
    print(groups)
    if created and len(groups)== 0:
        group = Group.objects.get(name = 'Vacataire')
        instance.groups.add(group)
        Vacataire.objects.create(user = instance)
        print("le profile vacataire cree avec succees ....")


