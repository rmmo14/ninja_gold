from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('farmgold', views.farm),
    path('cavegold', views.cave),
    path('housegold', views.house),
    path('casinogold', views.casino),
]
