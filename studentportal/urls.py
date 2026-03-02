from django.contrib import admin
from django.urls import path
from portal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('students/', views.display_all, name='student_list'),
    path('add/', views.insert_student, name='add_student'),
    path('about/', views.about, name='about'),
    path('student/<int:student_id>/', views.display_one_student, name='student_detail'),
]