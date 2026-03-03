from django.shortcuts import render
import re

students = [
    {"id": 1, "name": "Rahul", "course": "Python", "email": "rahul@gmail.com", "class": "FY"},
    {"id": 2, "name": "Sneha", "course": "Java", "email": "sneha@gmail.com", "class": "SY"},
    {"id": 3, "name": "Amit", "course": "AI & ML", "email": "amit@gmail.com", "class": "TY"},
]


def home_view(request):
    courses = ["Python", "Java", "Software Testing", "AI & ML"]
    return render(request, 'portal/home.html', {"courses": courses})


def student_list_view(request):
    return render(request, 'portal/student_list.html', {"students": students})


def add_student_view(request):
    message = ""
    error = ""

    if request.method == "POST":

        name = request.POST.get("name")
        course = request.POST.get("course")
        email = request.POST.get("email")
        student_class = request.POST.get("class")

        if not email:
            error = "Email is required"

        else:
            student_data = {
                "id": len(students) + 1,
                "name": name,
                "course": course,
                "email": email,
                "class": student_class
            }

            students.append(student_data)

            print("NEW STUDENT ADDED:")
            print(student_data)

            message = "Student Added Successfully!"

    return render(request, "portal/add_student.html",
                  {"message": message, "error": error})


def login_view(request):
    message = ""
    error = ""

    if request.method == "POST":
        email = request.POST.get("userid")
        password = request.POST.get("password")

        if len(password) < 8:
            error = "Password must be at least 8 characters"
        else:
            login_data = {
                "email": email,
                "password": password
            }

            print("LOGIN DATA:")
            print(login_data)

            message = "Login Successful!"

    return render(request, 'portal/login.html',
                  {"message": message, "error": error})

def register_view(request):
    message = ""
    error = ""

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        mobile = request.POST.get("mobile")
        dob = request.POST.get("dob")
        student_class = request.POST.get("class")
        gender = request.POST.get("gender")

        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(email_pattern, email):
            error = "Invalid Email Format"

        elif not mobile.isdigit() or len(mobile) != 10:
            error = "Mobile number must be 10 digits"

        elif len(password) < 8:
            error = "Password must be at least 8 characters"

        else:
            register_data = {
                "name": name,
                "email": email,
                "password": password,
                "mobile": mobile,
                "dob": dob,
                "class": student_class,
                "gender": gender
            }

            print("REGISTER DATA:")
            print(register_data)

            message = "Registration Successful!"

    return render(request, 'portal/register.html',
                  {"message": message, "error": error})


def about_view(request):
    return render(request, 'portal/about.html')
def student_detail_view(request, id):
    student = next((s for s in students if s["id"] == id), None)
    return render(request, 'portal/student_detail.html', {"student": student})