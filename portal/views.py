from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect

# Global list (temporary storage)
students = []


# Home View
def home(request):
    return render(request, 'portal_s/home.html')


# About View
def about(request):
    return render(request, 'portal_s/about.html')


# Student List with Pagination
def student_list(request):

    page = int(request.GET.get("page", 1))
    per_page = 3   # students per page

    start = (page - 1) * per_page
    end = start + per_page

    paginated_students = students[start:end]

    total_pages = (len(students) + per_page - 1) // per_page

    success_message = request.GET.get("success")

    context = {
        "students": paginated_students,
        "page": page,
        "total_pages": total_pages,
        "success": success_message
    }

    return render(request, 'portal_s/student_list.html', context)


# Add Student
def add_student(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        course = request.POST.get('course')
        image = request.POST.get('image')   # Profile Image URL

        new_student = {
            "id": len(students) + 1,
            "name": name,
            "email": email,
            "age": age,
            "course": course,
            "image": image
        }

        students.append(new_student)

        # ✅ Correct redirect using URL name
        url = reverse('add_student')
        return HttpResponseRedirect(f"{url}?success=Student Added Successfully")

    return render(request, 'portal_s/add_student.html')


# Student Detail
def student_detail(request, id):

    student_data = None

    for student in students:
        if student["id"] == id:
            student_data = student
            break

    return render(request, 'portal_s/student_detail.html', {'student': student_data})


# Edit Student
def edit_student(request, id):

    student_data = None

    for student in students:
        if student["id"] == id:
            student_data = student
            break

    if request.method == "POST":
        student_data["name"] = request.POST.get("name")
        student_data["email"] = request.POST.get("email")
        student_data["age"] = request.POST.get("age")
        student_data["course"] = request.POST.get("course")
        student_data["image"] = request.POST.get("image")

        return redirect('student_detail', id=id)

    return render(request, 'portal_s/edit_student.html', {'student': student_data})


# Delete Student
def delete_student(request, id):
    global students

    # Remove student with matching id
    students = [student for student in students if student["id"] != id]

    # ✅ Correct redirect using URL name
    url = reverse('student_list')
    return HttpResponseRedirect(f"{url}?success=Student Deleted Successfully")