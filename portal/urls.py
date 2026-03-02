from django.urls import path
from . import views

app_name = 'portal'

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_list, name='student_list'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('add/', views.add_student, name='add_student'),
    path('about/', views.about, name='about'),
    path('base/', views.information, name='base'),
]
