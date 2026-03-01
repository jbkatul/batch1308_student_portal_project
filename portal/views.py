from django.shortcuts import render

# Create your views here.

def student_list(request):
    students = [{"id": 1, "name": "Rahul", "course": "django","email": "rahul@example.com"},
               {"id": 2, "name": "Priya", "course": "python","email": "priya@example.com"},
               {"id": 4, "name": "sayali", "course": "django","email": "sayali@example.com"} , 
               {"id": 5, "name": "divya", "course": "java","email": "divya@example.com"} ,    
                ]    




    return render(request, 'portal/student_list.html', {'students': students})   

def home(request):
    return render(request, "portal/home.html")


def student_detail(request, id):
    student = None
    for s in students:
        if s["id"] == id:
            student = s
    return render(request, "portal/student_detail.html", {"student": student})    

def search_student(request):
    query = request.GET.get("q")
    result = []

    if query:
        for s in students:
            if query.lower() in s["name"].lower():
                result.append(s)

    return render(request, "portal/student_list.html", {"students": result})    

def about(request):
    return render(request, "portal/about.html")    
             