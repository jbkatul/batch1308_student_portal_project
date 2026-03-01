from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage

def home(request):
    return render(request, "portal/home.html", {
        "student_count": len(student_db)})
def about_us(request):
    return render(request, "portal/about.html")


students = [
    {"id": 1, 
     "name": "Narendra", 
     "course": "Django", 
     "email": "narendra@gmail.com", 
     "photo":"https://th.bing.com/th/id/R.978b5f5e2c4b39de1c4a887310518134?rik=ysCyR3%2bNP08lDA&riu=http%3a%2f%2fi.huffpost.com%2fgen%2f4459084%2foriginal.jpg&ehk=KdYL%2bOcs1y5xC5tbCspW47E9IUieGx4Q6UXeqQL9KOI%3d&risl=&pid=ImgRaw&r=0"},


    {"id": 2, 
     "name": "Rahul",
     "course": "Python", 
     "email": "rahul@gmail.com", 
     "photo":"https://akm-img-a-in.tosshub.com/businesstoday/images/story/202303/rahul-g-1200-sixteen_nine.jpg"},

]
student_db = students.copy()
def student_list(request):
    search = request.GET.get("search")
    students_data = student_db

    if search:
        students_data = [
            s for s in student_db
            if search.lower() in s["name"].lower()
        ]

    return render(request, "portal/student_list.html", {"students": students_data})



def add_student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        course = request.POST.get("course")
        email = request.POST.get("email")
        photo = request.FILES.get("photo")

        photo_url = None

        if photo:
            fs = FileSystemStorage()
            filename = fs.save(photo.name, photo)
            photo_url = fs.url(filename)

        student = {
            "id": len(student_db) + 1,
            "name": name,
            "course": course,
            "email": email,
            "photo": photo_url
        }

        student_db.append(student)

        return redirect("students")

    return render(request, "portal/add_student.html")

def student_detail(request, id):
    for s in student_db:
        if s["id"] == id:
            student = s
            break
    return render(request, "portal/student_detail.html", {"student": student})



