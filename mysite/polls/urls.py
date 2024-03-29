from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    #ex:/polls/create
    path('create/',views.create,name='create'),
    #ex:/polls/deleted
    path('<int:question_id>/delete/', views.delete, name='delete'),
    #ex:/polls/updated
    path('<int:question_id>/update/', views.update, name='update'),
    #ex:/polls/createusingp
    path('createusingp/',views.createusingp,name='createusingp'),
    #ex:/polls/form
    path('form/',views.form,name='form'),
    #ex:/polls/create
    path('createnewquestion/',views.createnewquestion,name='createnewquestion'),
    
]