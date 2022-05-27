from operator import truediv
from django.db import models

class Student(models.Model):
    nazwa = models.CharField(max_length=90)
    Wiek = models.TextField(blank=True)
    dataurodzenia = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.nazwa
    
class kurs(models.Model):
     nazwa = models.CharField(max_length=80)
     students = models.ManyToManyField(Student,through='Rejestracja')

     def __str__(self):
        return self.nazwa

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Sklepik(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.nazwa


class Rejestracja(models.Model):
        Student = models.ForeignKey(Student, on_delete=models.CASCADE)
        kurs = models.ForeignKey(kurs, on_delete=models.CASCADE)
        date_Rejestracja = models.DateField()
        Koncowa_ocena = models.CharField(max_length=1, blank=True, null=True)

