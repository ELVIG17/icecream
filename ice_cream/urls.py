from django.urls import path
from . import views

app_name = 'ice_cream'

urlpatterns = [
    # Список мороженого. name совпадает с views.ice_cream_list
    path('', views.ice_cream_list, name='ice_cream_list'),
    
    # Детальная страница. name совпадает с views.ice_cream_detail
    # Обратите внимание: параметр называется pk, так как мы использовали его в views
    path('<int:pk>/', views.ice_cream_detail, name='ice_cream_detail'),
]
