from django.shortcuts import render
from .models import ExamCenter, Student

def home(request):
    exam_center = ExamCenter.objects.all()
    student_data = Student.objects.all()
    return render(request, 'school/home.html', {'centers': exam_center, 'students': student_data})
