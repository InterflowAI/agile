# quiz/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('personality/', views.index, name='index'),  # Home page, redirects to quiz
    
  # URL to start quiz (optional)
    path('result/', views.result, name='result'),  # URL to display result
    path ('careerquiz/',views.careerquiz,name='careerquiz'),
    path('careerresult/', views.careerquiz, name='careerresult')
]
