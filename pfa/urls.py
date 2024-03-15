"""pfa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.views import Login, Logout
from Service.views import Home,  Add, CreateProfile, Details , ManageFiliere , filiereDetails


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    path('login', Login, name = 'login'),
    path('logout', Logout, name= 'logout'), 

    path('', Home, name='home'),

    path('fichier_notes',ManageFiliere, name= 'cours' ),
    path('filiereDetails/<str:name>/',filiereDetails, name= 'filiere' ),



    path('add_vacataire', Add , name = 'add' ),
    path('create_profile/<str:pk>/', CreateProfile, name= 'create'),


    path('details/<str:name>', Details, name = 'details')


]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
