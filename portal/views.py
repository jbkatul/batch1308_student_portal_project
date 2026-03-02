from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest

# Basic views to render the existing templates in portal/templates/portal/
def home(request: HttpRequest):
	return render(request, 'portal/home.html')


def student_list(request: HttpRequest):
	return render(request, 'portal/student_list.html')


def student_detail(request: HttpRequest, pk: int):
	# Placeholder: templates expect a context object named `student`.
	# Since no model exists in this starter project, pass an empty dict.
	return render(request, 'portal/student_detail.html', {'student': {}})


def add_student(request: HttpRequest):
	if request.method == 'POST':
		# No form processing yet — redirect back to list for now
		return redirect('portal:student_list')
	return render(request, 'portal/add_student.html')


def about(request: HttpRequest):
	return render(request, 'portal/about.html')


def information(request: HttpRequest):
	return render(request, 'portal/base.html')
