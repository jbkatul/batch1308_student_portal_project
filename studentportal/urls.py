from django.urls import path
from portal.views import * 

urlpatterns = [
    path('', home),
    path('students/', student_list),
    path('student/<int:id>/', student_detail),
    path('add/', add_student),
    path('search/', search_student),
    path('about/', about),
]