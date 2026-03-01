from django.shortcuts import render, redirect

students = [
    {
        "id": 1,
        "name": "Rahul Sharma",
        "age": 21,
        "department": "Computer Science",
        "grade": "A",
        "email": "rahul@gmail.com",
        "phone": "9876543210"
    },
    {
        "id": 2,
        "name": "Sneha Patil",
        "age": 22,
        "department": "Information Technology",
        "grade": "B",
        "email": "sneha@gmail.com",
        "phone": "9123456780"
    },
    {
        "id": 3,
        "name": "Amit Kumar",
        "age": 20,
        "department": "Electronics",
        "grade": "A",
        "email": "amit@gmail.com",
        "phone": "9876543211"
    },
    {
        "id": 4,
        "name": "Priya Singh",
        "age": 21,
        "department": "Mechanical",
        "grade": "B",
        "email": "priya@gmail.com",
        "phone": "9876543212"
    },
    {
        "id": 5,
        "name": "Vikram Joshi",
        "age": 22,
        "department": "Civil",
        "grade": "A",
        "email": "vikram@gmail.com",
        "phone": "9876543213"
    }
]



def home(request):
    return render(request, "portal/home.html")



def about(request):
    return render(request, "portal/about.html")



def student_list(request):
    return render(request, "portal/student_list.html", {"students": students})



def student_detail(request, id):
    student = next((s for s in students if s["id"] == id), None)
    return render(request, "portal/student_detail.html", {"student": student})



def add_student(request):
    
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        department = request.POST.get("department")
        grade = request.POST.get("grade")
        phone = request.POST.get("phone")

        new_student = {
            "id": len(students) + 1,
            "name": name,
            "age": age,
            "department": department,
            "grade": grade,
            "email": email,
            "phone": phone
        }

        students.append(new_student)

        return redirect("student_list")

    return render(request, "portal/add_student.html")  


def edit_student(request, id):
    
    student = next((s for s in students if s["id"] == id), None)

    if request.method == "POST":
        student["name"] = request.POST.get("name")
        student["email"] = request.POST.get("email")
        student["department"] = request.POST.get("department")
        student["phone"] = request.POST.get("phone")

        return redirect("student_list")

    return render(request, "portal/edit_student.html", {"student": student})


def delete_student(request, id):
    global students

    if request.method == "POST":
        students = [s for s in students if s["id"] != id]

    return redirect("student_list")