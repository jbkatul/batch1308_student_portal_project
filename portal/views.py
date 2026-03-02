from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'portal/home.html')


def student_list(request):
    # placeholder: later fetch students from database
    return render(request, 'portal/student_list.html')


def add_student(request):
    # placeholder: form to add a student
    return render(request, 'portal/add_student.html')


def about(request):
    return render(request, 'portal/about.html')
