from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'portal/home.html')

def student_list_view(request):
    return render(request, 'portal/student_list.html')

def about_view(request):
    return render(request, 'portal/about.html')
def home_view(request):
    return render(request, 'portal/home.html')
def student_list_view(request):

    students = [
        {"id": 1, "name": "Rahul", "course": "Python", "email": "rahul@gmail.com"},
        {"id": 2, "name": "Sneha", "course": "Django", "email": "sneha@gmail.com"},
        {"id": 3, "name": "Amit", "course": "Java", "email": "amit@gmail.com"},
    ]

    return render(request, 'portal/student_list.html', {"students": students})