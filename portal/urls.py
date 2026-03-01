from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('students/', views.student_list, name="student_list"),
    path('student/<int:id>/', views.student_detail, name="student_detail"),
    path('add/', views.add_student, name="add_student"),
    path('search/', views.search_student, name="search_student"),
    path('about/', views.about, name="about"),
    path('delete/<int:id>/', views.delete_student, name="delete_student"),
]