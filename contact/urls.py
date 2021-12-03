from django.urls import path
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from . import views

urlpatterns = [
    path('',views.read_contacts),
    path('<int:id>/',views.read_contact),
    path('<int:id>/',views.edit_contact),
    path('<int:id>/',views.delete_contact),
    path('',csrf_protect(views.create_contact) ),

]
