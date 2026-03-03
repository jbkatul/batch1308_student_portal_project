from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

def home(request):
    return render(request, 'portal/home.html')

def about(request):
    return render(request, 'portal/about.html')

def student_list(request):
    students = Student.objects.all().order_by('-id')
    return render(request, 'portal/student_list.html', {'students': students})

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'portal/student_detail.html', {'student': student})

def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        course = request.POST.get('course')
        
        # Save into the database
        Student.objects.create(name=name, age=age, course=course)
        
        # Redirect back to the student list to see the update
        return redirect('student_list')
        
    return render(request, 'portal/add_student.html')

