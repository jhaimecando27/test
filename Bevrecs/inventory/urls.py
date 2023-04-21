from django.urls import path

from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_ingridients', views.addIngridients, name='add_ingridients'),
]
