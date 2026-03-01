
from django.contrib import admin
from django.urls import path
from portal.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', student_list, name='student_list'),
    path('HOME', home_views, name='home'),
]
