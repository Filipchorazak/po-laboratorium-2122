
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('pollss.urls')),
    path('admin/', admin.site.urls),
    #path('kurs/',include('przedmioty.urls',namespace='kurs')),

]
