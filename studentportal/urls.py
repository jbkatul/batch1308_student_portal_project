from django.contrib import admin
from django.urls import path
from portal.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', home_view, name='home'),
    path('students/', student_list_view, name='student_list'),
    path('student/<int:id>/', student_detail_view, name='student_detail'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('about/', about_view, name='about'),
    path('add-student/', add_student_view, name='add_student'),
]