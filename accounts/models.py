from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser , Group
)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            email= email,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            **extra_fields
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user




class User(AbstractBaseUser):


    cin = models.CharField( max_length=50, primary_key = True)
    name = models.CharField(max_length=125)
    date_created = models.DateTimeField(auto_now_add= True)
    last_login = models.DateTimeField(blank=True, null=True)

    email = models.EmailField( 
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser

    groups = models.ManyToManyField(Group)

   


    objects = UserManager() 

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name'] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.name
    
    def get_first_name(self):
        # The user is identified by their email address
        return self.name.split()[0]
    
    def get_last_name(self):
        # The user is identified by their email address
        return self.name.split()[1]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin




  
   

