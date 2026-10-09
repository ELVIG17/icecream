from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    # name совпадает с функцией views.description
    path('', views.description, name='description'),
]
