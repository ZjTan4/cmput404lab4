from django.urls import path
from . import views

'''
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
'''
# Question 8
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

