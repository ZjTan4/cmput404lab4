from django.urls import path
from . import views

urlpatterns = [
    
    # Question 3
    # /polls/
    path('', views.index, name='index'), 

    # Question 6
    # /polls/<question_id>/
    # /polls/<question_id>/results/
    # /polls/<question_id>/vote/
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]