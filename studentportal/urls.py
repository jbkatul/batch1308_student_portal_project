from django.contrib import admin
from django.urls import path
from portal.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('students/', student_list, name='student_list'),
    path('search/', search_student, name='search_student'),
   path('s/<int:id>/', student_detail, name='student_detail'),
   path('add/', add_student, name='add_student'),
   path('student/delete/<int:id>/', delete_student, name='delete_student'),
   path('about/', about, name='about'),
]
