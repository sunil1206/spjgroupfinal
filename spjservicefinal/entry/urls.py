from django.urls import path
from . import views

urlpatterns = [

    path('entry/', views.adminpanel, name='entry'),
    path('apply/', views.apply, name='apply')
    ]