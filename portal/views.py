from django.shortcuts import render

def home_view(request):
    return render(request, 'portal/home.html')

def about(request):
    return render(request, 'portal/about.html')

def display_all(request):
    # Here you can fetch students from database later
    return render(request, 'portal/students.html')

def insert_student(request):
    # Here you can add form handling later
    return render(request, 'portal/add_student.html')

def display_one_student(request, student_id):
    # Later you can fetch a single student by ID
    return render(request, 'portal/student_detail.html', {'student_id': student_id})

# Example student data (replace later with database models)
students_data = [
    {"id": 1, "name": "Madhura", "roll": "101", "branch": "Computer Science", "photo": "https://via.placeholder.com/150"},
    {"id": 2, "name": "Mayuri", "roll": "102", "branch": "Mechanical", "photo": "https://via.placeholder.com/150"},
    {"id": 3, "name": "Shruti", "roll": "103", "branch": "Electrical", "photo": "https://via.placeholder.com/150"},
]

def display_all(request):
    return render(request, 'portal/student_list.html', {'students': students_data})

def display_one_student(request, student_id):
    student = next((s for s in students_data if s["id"] == student_id), None)
    return render(request, 'portal/student_detail.html', {'student': student})