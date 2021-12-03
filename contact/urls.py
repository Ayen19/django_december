from django.urls import path
from rest_framework import routers
from . import views

urlpatterns = [
    path('get-contacts/', (views.read_contacts)),
    path('create-contact/', (views.create_contact)),
    path('edit-contact/<int:id>/',views.edit_contact),
    path('get-contact/<int:id>/',views.read_contact),
    path('delete-contact/<int:id>/',views.delete_contact),
]
