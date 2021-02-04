from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    student_data = Student.students.all()
    return render(request, 'school/home.html', {'students': student_data})
