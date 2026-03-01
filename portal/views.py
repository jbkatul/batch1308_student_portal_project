from django.shortcuts import render, redirect
from django.contrib import messages

# List as Database
students = [
    {
        "id": 1,
        "name": "Rahul Yadav",
        "course": "Python",
        "email": "rahul@gmail.com",
        "photo": "https://randomuser.me/api/portraits/men/32.jpg"
    },
    {
        "id": 2,
        "name": "Sneha Sharma",
        "course": "Django",
        "email": "sneha@gmail.com",
        "photo": "https://randomuser.me/api/portraits/women/44.jpg"
    },
]

# Home Page
def home(request):
    return render(request, "portal/home.html")


# About Page
def about(request):
    return render(request, "portal/about.html")


# Student List
def student_list(request):
    return render(request, "portal/student_list.html", {"students": students})


# Student Detail
def student_detail(request, id):
    student = None
    for s in students:
        if s["id"] == id:
            student = s
    return render(request, "portal/student_detail.html", {"student": student})


# Add Student
def add_student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        course = request.POST.get("course")
        email = request.POST.get("email")

        new_student = {
            "id": len(students) + 1,
            "name": name,
            "course": course,
            "email": email,
            "photo": "https://randomuser.me/api/portraits/lego/1.jpg"
        }

        students.append(new_student)
        messages.success(request, "✅ Student Added Successfully!")
        return redirect("student_list")

    return render(request, "portal/add_student.html")


# Search Student
def search_student(request):
    query = request.GET.get("q")
    result = []

    if query:
        for s in students:
            if query.lower() in s["name"].lower():
                result.append(s)

    return render(request, "portal/student_list.html", {"students": result})

def delete_student(request, id):
    global students
    students = [s for s in students if s["id"] != id]
    messages.error(request, "❌ Student Deleted Successfully!")
    return redirect("student_list")