from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('students/', views.student_list, name='student_list'),
    path('student/<int:id>/', views.student_detail, name='student_detail'),
    path('add-student/', views.add_student, name='add_student'),
]
