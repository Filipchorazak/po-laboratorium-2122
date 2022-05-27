from django.urls import *
from . import views


urlpatterns = [
    path('Student',views.Studentview.as_view(),name='index'),
    path('kurs',views.kursview.as_view(),name='index'),    
]

