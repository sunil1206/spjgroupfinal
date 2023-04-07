from django.urls import path
from . import views


urlpatterns=[
    path('',views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('readmore/<int:service_id>/', views.detail, name='detail'),
    path('status/', views.status, name='status'),
    path('gallery/', views.gallery_page, name='gallery'),
    path('associate/', views.Associate, name='associate')
]
