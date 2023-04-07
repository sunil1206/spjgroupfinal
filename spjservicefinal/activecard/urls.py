from django.contrib import admin
from django.urls import path
# from .views import rightcard

from . import views

urlpatterns = [
    path('card_details/', views.get_card_details, name='card_details'),

    path('rightcard/', views.rightcard, name='active_card'),
    # path('reg/', views.register, name='qr_scaner')

]