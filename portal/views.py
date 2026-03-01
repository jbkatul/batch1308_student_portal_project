from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect

# Temporary Database (List + Dictionary)
student_db = [
    {"id": 1, "name": "Rahul", "course": "Python", "email": "rahul@gmail.com"},
    {"id": 2, "name": "Sneha", "course": "Django", "email": "sneha@gmail.com"},
]

# HOME
def home(request):
    return render(request, "portal/home.html")

# ABOUT
def about(request):
    return render(request, "portal/about.html")

# STUDENT LIST
def student_list(request):
    return render(request, "portal/student_list.html", {
        "students": student_db
    })

# STUDENT DETAIL
def student_detail(request, id):
    student = None
    for s in student_db:
        if s["id"] == id:
            student = s

    return render(request, "portal/student_detail.html", {
        "student": student
    })

# ADD STUDENT
def add_student(request):

    if request.method == "POST":
        name = request.POST.get("name")
        course = request.POST.get("course")
        email = request.POST.get("email")

        student = {
            "id": len(student_db) + 1,
            "name": name,
            "course": course,
            "email": email
        }

        student_db.append(student)

        return redirect("students")

    return render(request, "portal/add_student.html")

# SEARCH STUDENT
def search_student(request):
    query = request.GET.get("q")
    results = []

    if query:
        for s in student_db:
            if query.lower() in s["name"].lower():
                results.append(s)

    return render(request, "portal/student_list.html", {
        "students": results
    })