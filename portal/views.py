from django.shortcuts import render

# Temporary Database
students = [
    {"id": 1, "name": "Rahul", "course": "Python", "email": "rahul@gmail.com"},
    {"id": 2, "name": "Sneha", "course": "Django", "email": "sneha@gmail.com"},
]

student_db = []


def home(request):
    return render(request, "portal/home.html")


def about(request):
    return render(request, "portal/about.html")


def student_list(request):
    return render(request, "portal/student_list.html", {"students": students + student_db})


def student_detail(request, id):
    all_students = students + student_db
    student = None

    for s in all_students:
        if s["id"] == id:
            student = s

    return render(request, "portal/student_detail.html", {"student": student})


def add_student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        course = request.POST.get("course")
        email = request.POST.get("email")

        new_student = {
            "id": len(students) + len(student_db) + 1,
            "name": name,
            "course": course,
            "email": email
        }

        student_db.append(new_student)

    return render(request, "portal/add_student.html")


def search_student(request):
    query = request.GET.get("q")
    all_students = students + student_db
    result = []

    if query:
        for s in all_students:
            if query.lower() in s["name"].lower():
                result.append(s)

    return render(request, "portal/student_list.html", {"students": result})