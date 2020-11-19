from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('gold', views.process),
    path('reset', views.reset),
]
