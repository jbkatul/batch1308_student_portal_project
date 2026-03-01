from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def student_list(request):
    students = [
        {"id": 1, "name": "Rahul", "course": "Python", "email": "Rahul@gmail.com"},
        {"id": 2, "name": "Sneha", "course": "Django", "email": "Sneha@gmail.com"},
        {"id": 3, "name": "Rohan", "course": "python", "email": "Rohan@gmail.com"},
        {"id": 4, "name": "Prem", "course": "Java",     "email": "Prem@gmail.com"},
        {"id": 5, "name": "Khushi", "course": "AL/ML", "email": "Khushi@gmail.com"},
        {"id": 6, "name": "kajal", "course": "Python", "email": "kajal@gmail.com"},
        {"id": 7, "name": "Vaishu", "course": "Django", "email": "Vaishu@gmail.com"},
        {"id": 8, "name":   "Om",   "course": "Java",   "email": "Om@gmail.com"},
        {"id": 9, "name": "Shruti", "course": "C++",     "email": "Shruti@gmail.com"},
        {"id": 10, "name": "Sahili", "course": "AL/ML", "email": "Sahili@gmail.com"},


    ]
    
    return render(request, "portal/student_list.html", {"students": students})

def home_views(request):
    return render(request, "portal/home.html")
