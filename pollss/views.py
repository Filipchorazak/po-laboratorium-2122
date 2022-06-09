from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Student, kurs, Rejestracja
# Create your views here


class Studentview(generic.ListView):
    nazwa=Student
    template_name='Student_list.html'
    def get_queryset(self):
        return Student.objects.all()

class kursview(generic.ListView):
    nazwa=kurs
    template_name='kurs_list.html'
    def get_queryset(self):
        return kurs.objects.all()



class Rejestracjaview(generic.ListView):
    nazwa=Rejestracja
    template_name='Rejestracja_list.html'
    def get_queryset(self):
        return Rejestracja.objects.all()

