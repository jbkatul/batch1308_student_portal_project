from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request, 'portal/home.html')

students = [
    {"id": 1, "name": "Rahul", "course": "Python", "email": "rahul@gmail.com"},
    {"id": 2, "name": "Sneha", "course": "Django", "email": "sneha@gmail.com"},
    {"id": 3, "name": "Ankit", "course": "JavaScript", "email": "ankit@gmail.com"},
    {"id": 4, "name": "Ranjan", "course": "React", "email": "ranjan@gmail.com"},
    {"id": 5, "name": "Savi", "course": "Bootstrap", "email": "savi@gmail.com"},


]

def student_list(request):
    page = int(request.GET.get("page", 1))  # current page, default 1
    per_page = 5
    start = (page - 1) * per_page
    end = start + per_page

    total_students = len(students)
    total_pages = (total_students + per_page - 1) // per_page  # ceil division

    students_paginated = students[start:end]

    context = {
        "students": students_paginated,
        "page": page,
        "total_pages": total_pages
    }
    return render(request, "portal/student_list.html", context)

def search_student(request):
    query = request.GET.get("q", "")
    result = []

    for s in students:
        if query.lower() in s["name"].lower():
            result.append(s)

    return render(request, "portal/student_list.html", {"students": result})

def student_detail(request, id):
    student = None
    for s in students:
        if s["id"] == id:
            student = s
            break
    return render(request, "portal/student_detail.html", {"student": student})

def add_student(request):
    message = ""
    if request.method == "POST":
        name = request.POST.get("name")
        course = request.POST.get("course")
        email = request.POST.get("email")

        student = {
            "id": len(students) + 1,
            "name": name,
            "course": course,
            "email": email
        }
        students.append(student)
        message = "Student added successfully!"

    return render(request, "portal/add_student.html", {"message": message})

def delete_student(request, id):
    global students
    students = [s for s in students if s["id"] != id]
    return redirect('student_list')

def about(request):
    return render(request, "portal/about.html")