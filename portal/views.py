from django.shortcuts import render, redirect

# Create your views here.

from django.shortcuts import render, redirect

students = [
    {"id": 1, "name": "Sana", "course": "Python", "email": "sana@gmail.com"},
    {"id": 2, "name": "Aman", "course": "Django", "email": "aman@gmail.com"},
    {"id": 3, "name": "Saif", "course": "Python", "email": "saif@gmail.com"},
    {"id": 4, "name": "Tanu", "course": "Python", "email": "tanu@gmail.com"},
    {"id": 5, "name": "Rashmi", "course": "Django", "email": "tanu@gmail.com"},
    {"id": 6, "name": "Joseph", "course": "Python", "email": "tanu@gmail.com"},
    {"id": 7, "name": "Kalyani", "course": "Python", "email": "tanu@gmail.com"},
    {"id": 8, "name": "Aiman", "course": "Django", "email": "tanu@gmail.com"},
    {"id": 9, "name": "Suresh", "course": "Python", "email": "tanu@gmail.com"},
    {"id": 10, "name": "Alina", "course": "Python" , "email": "tanu@gmail.com"},
    {"id": 11, "name": "Kareena", "course": "Django", "email": "tanu@gmail.com"},
    {"id": 12, "name": "Simran", "course": "Java", "email": "tanu@gmail.com"},
    {"id": 13, "name": "Ritu", "course": "Java", "email": "tanu@gmail.com"},
    
    
    
    
]


def home(request):
    return render(request, 'portal/home.html')

def student_list(request):
    return render(request, "portal/student_list.html", {"students": students})

def search_student(request):
    query = request.GET.get("q", "")
    result = [s for s in students if query.lower() in s["name"].lower()]
    return render(request, "portal/student_list.html", {"students": result})

def student_detail(request, id):
    student = next((s for s in students if s["id"] == id), None)
    return render(request, "portal/student_detail.html", {"student": student})

def add_student(request):
    if request.method == "POST":
        new_student = {
            "id": len(students) + 1,
            "name": request.POST.get("name"),
            "course": request.POST.get("course"),
            "email": request.POST.get("email"),
        }
        students.append(new_student)
        return redirect("student_list")
    return render(request, "portal/add_student.html")

def delete_student(request, id):
    global students
    students = [s for s in students if s["id"] != id]
    return redirect("student_list")

def about(request):
    return render(request, "portal/about.html")