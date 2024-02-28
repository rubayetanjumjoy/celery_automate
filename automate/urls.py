
from django.urls import path
from . import views

urlpatterns = [
    path('automate/', views.automate_view, name='index'),

     
]