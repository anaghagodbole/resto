from django.urls import path

from . import views

urlpatterns = [
   # path('', views.index, name='index'),
   # path('', views.index, name='index'),
    #ex:/polls/form
    path('form/',views.form,name='form'),
    #ex:/polls/create
    path('create/',views.create,name='create'),
    path('<int:restaurant_id>/',views.detail, name='detail'),
    #ex:/restaurant/show
    path('<int:restaurant_id>/additem/',views.additem, name='additem'),
   
   
   
]