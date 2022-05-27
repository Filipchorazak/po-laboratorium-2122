from django.contrib import admin
from .models import Sklepik
from .models import Student, kurs
from .models import Rejestracja
# Register your models here.


admin.site.register(Sklepik)
admin.site.register(Student)
admin.site.register(kurs)
admin.site.register(Rejestracja)



