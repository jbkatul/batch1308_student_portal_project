from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Student

def registration(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")
        
        if pass1 != pass2:
            return render(request, "portal/registration.html", {"mismatch":"Passwords do not match"})
        else:
            if User.objects.filter(username = username, email = email).exists():
                return render(request, "portal/registration.html", {"both_taken":"Username and email has been taken already"})
            elif User.objects.filter(email = email).exists():
                return render(request, "portal/registration.html", {"email_taken": "Email has been already registered you may login"})
            elif User.objects.filter(username = username).exists():
                return render(request, "portal/registration.html", {"U_taken":"Username is already taken please use another one"})
        
            user = User.objects.create_user(
                username = username,
                email = email,
                password = pass1
                )
        
            user.save()
            return redirect('login')

    return render(request, "portal/registration.html")

def login_view(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("home")
        else:
            return render(request, "portal/login.html", {"error":"Invalid Username of Password"})
    return render(request, "portal/login.html")

def logout(request):
    return render(request, "portal/login.html")

@login_required
def home(request):
    students = Student.objects.count()
    return render(request, "portal/home.html", {"student_count": students})

@login_required
def about_us(request):
    return render(request, "portal/about.html")


@login_required
def student_list(request):
    search = request.GET.get("search")
    students_data = Student.objects.all()

    if search:
        students_data = students_data.filter(name__icontains=search)

    return render(request, "portal/student_list.html", {"students": students_data})


@login_required
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

        
        student = Student.objects.create(
            name=name,
            course=course,
            email=email,
            photo=photo_url
        )
        student.save()

        return redirect("students")

    return render(request, "portal/add_student.html")


@login_required
def student_detail(request, id):
    student = Student.objects.get(id=id)
    return render(request, "portal/student_detail.html", {"student": student})



