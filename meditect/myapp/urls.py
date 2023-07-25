from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('bmi/', views.bmi , name='bmi'),
    path('diabeticdisease/', views.diabeticdisease , name='diabeticdisease'),
    path('diabeticretinopathy/', views.diabeticretinopathy , name='diabeticretinopathy'),
    path('alzheimers/', views.alzheimers , name='alzheimers'),
    path('skindisease/', views.skindisease , name='skindisease'),
    path('ReadMoreAboutAI/', views.ReadMoreAboutAI , name='ReadMoreAboutAI'),
    path('heartdisease/', views.heartdisease , name='heartdisease'),

]
