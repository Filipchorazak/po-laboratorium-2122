from operator import truediv
from django.db import models
import datetime

class Student(models.Model):
    Imie = models.CharField(max_length=200)
    Nazwisko = models.CharField(max_length=200)
    Pesel = models.TextField(blank=True)
    data_urodzenia = models.DateField(default=None)

    def __str__(self):
        return f'{self.Imie} {self.Nazwisko}'

    class Meta:
        verbose_name_plural="Student"
    
class kurs(models.Model):
    nazwa = models.CharField(max_length=80)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.nazwa
    
    class Meta:
        verbose_name_plural="kurs"
    
    

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    

    




class Rejestracja(models.Model):
        
        Student = models.ForeignKey(Student, on_delete=models.CASCADE)
        kurs = models.ForeignKey(kurs, on_delete=models.CASCADE)
        data_Rejestracji = models.DateField()
        Koncowa_ocena = models.CharField(max_length=1, blank=True, null=True)
        Opinia_od_wychowawcy = models.TextField(blank=True)
        
        #def __str__(self):
         #return self.Student
        
        class Meta:
           verbose_name_plural = "Rejestracja"