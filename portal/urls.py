from django.contrib import admin
from django.urls import path
from portal.views import *

urlpatterns = [
    path("",home,name="home"),
    path('add-student/', add_student, name='add_student'),
    path('student_list/', student_list, name='student_list'),
    path("student_detail/<int:id>/", student_detail, name="student_detail"),  # <-- Add this
    path("about/", about, name="about"), 
]