from django.urls import path
from . import views

app_name = 'homepage' 

urlpatterns = [
    # name должен совпадать с именем функции views.index
    path('', views.index, name='index'),
]
