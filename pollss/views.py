from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import *
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." 
    % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)



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

