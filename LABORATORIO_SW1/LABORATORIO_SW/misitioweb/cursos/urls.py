from . import views
from django.urls import path, include 
urlpatterns=[
    path('', views.Lista_De_Cursos),
    path('<int:pk>', views.course_detail),
    
]