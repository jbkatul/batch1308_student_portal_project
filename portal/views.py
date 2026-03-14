from django.shortcuts import render, redirect

# Global list to store student data
student_db = [
    {"id": 1, "name": "Aman Khan", "course": "Computer Science", "email": "aman@example.com"},
    {"id": 2, "name": "Om karale", "course": "Information Technology", "email": "om@example.com"},
]

def home(request):
    return render(request, 'portal/home.html')

def student_list(request):
    return render(request, 'portal/student_list.html', {'students': student_db})

def student_detail(request, id):
    student = next((s for s in student_db if s['id'] == id), None)
    if student:
        return render(request, 'portal/student_detail.html', {'student': student})
    return render(request, 'portal/student_detail.html', {'error_message': 'Student not found.'})

def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        course = request.POST.get('course')
        email = request.POST.get('email')
        
        # Generated new ID
        new_id = len(student_db) + 1 if student_db else 1
        
        # Add to global list
        student_db.append({
            "id": new_id,
            "name": name,
            "course": course,
            "email": email
        })
        
        return redirect('student_list')
        
    return render(request, 'portal/add_student.html')

def search_student(request):
    query = request.GET.get("q", "").strip() # Get the search term
    results = []

    if query:
        for s in student_db:
            # Convert everything to strings for comparison
            s_id = str(s.get("id", ""))
            s_name = str(s.get("name", "")).lower()
            s_email = str(s.get("email", "")).lower()
            s_course = str(s.get("course", "")).lower()
            search_term = query.lower()

            # Check if query matches ID, Name, or Email
            if search_term == s_id or search_term in s_name or search_term in s_email or search_term in s_course:
                results.append(s)
    else:
        # If search is empty, show all students
        results = student_db

    return render(request, "portal/student_list.html", {"students": results, "query": query})

def about(request):
    return render(request, 'portal/about.html')
