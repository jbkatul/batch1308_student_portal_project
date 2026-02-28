from django.shortcuts import render


# Create your views here.
def home(request):
    students = [
        {'roll': 1, 'name': 'Alice', 'marks': 85},
        {'roll': 2, 'name': 'Bob', 'marks': 90},
        {'roll': 3, 'name': 'Charlie', 'marks': 78},
        {'roll': 4, 'name': 'David', 'marks': 92},
        {'roll': 5, 'name': 'Eve', 'marks': 88},
        {'roll': 1, 'name': 'Alice', 'marks': 85},
        {'roll': 2, 'name': 'Bob', 'marks': 90},
        {'roll': 3, 'name': 'Charlie', 'marks': 78},
        {'roll': 4, 'name': 'David', 'marks': 92},
        {'roll': 5, 'name': 'Eve', 'marks': 88},
    ]

    context = {
        'total_students': len(students)
    }
    return render(request, 'portal/home.html', context)


def student_list(request):
    students = [
        {'roll': 1, 'name': 'Alice', 'marks': 85},
        {'roll': 2, 'name': 'Bob', 'marks': 90},
        {'roll': 3, 'name': 'Charlie', 'marks': 78},
        {'roll': 4, 'name': 'David', 'marks': 92},
        {'roll': 5, 'name': 'Eve', 'marks': 88},
        {'roll': 1, 'name': 'Alice', 'marks': 85},
        {'roll': 2, 'name': 'Bob', 'marks': 90},
        {'roll': 3, 'name': 'Charlie', 'marks': 78},
        {'roll': 4, 'name': 'David', 'marks': 92},
        {'roll': 5, 'name': 'Eve', 'marks': 88},
    ]
    context = {
        'data': students,
        'total_students': len(students)   # ✅ correct
    }
    return render(request,'portal/student_list.html',context)


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
        print(name, course, email)

    return render(request, "portal/add_student.html")