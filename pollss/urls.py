from django.urls import path
from . import views
from .models import Student, kurs, Rejestracja

app_name = 'Pollss'
urlpatterns = [
    path('Student',views.Studentview.as_view(),name='index'),
    path('kurs',views.kursview.as_view(),name='index'),
    path('Rejestracja',views.Rejestracjaview.as_view(),name='index'),
    
]



