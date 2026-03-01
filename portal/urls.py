from django.urls import path
from portal import views
from portal.views import *

urlpatterns = [
    path('', home,name='home'),
    path('about/', about,name='about'),
    path('add-student/', views.add_student, name='add_student'),
    path('student/<int:id>/', views.student_detail, name='student_detail'),
    path('students/', views.student_list, name='student_list'),
    path('student/<int:id>/', views.student_detail, name='student_detail'),
   path('student/edit/<int:id>/', views.edit_student, name='edit_student'),
  path('student/delete/<int:id>/', views.delete_student, name='delete_student'),
  path('edit_student/<int:id>/', views.edit_student, name='edit_student'),
    
]