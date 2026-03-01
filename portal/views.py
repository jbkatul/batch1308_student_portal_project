
from django.shortcuts import render

# Temporary Database (List)
student_db = []

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

        return render(request, "portal/add_student.html", {
            "success": True,
            "students": student_db
        })

    return render(request, "portal/add_student.html")

    