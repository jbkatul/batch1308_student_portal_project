from django.shortcuts import render

# Home page
def home(request):
    return render(request, "portals/home.html")


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
            "email": email,
        }
        student_db.append(student)

    return render(request, "portals/add_student.html")


def student_list(request):
    return render(request, "portals/student_list.html", {
        "students": student_db
    })


def student_detail(request, id):
    student = None

    for s in student_db:
        if s["id"] == id:
            student = s
            break

    return render(request, "portals/student_detail.html", {
        "student": student
    })
    
def about(request):
    return render(request, "portals/about.html")