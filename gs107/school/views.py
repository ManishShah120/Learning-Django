from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    student_data = Student.students.get_stu_roll_range(103, 106)
    # student_data = Student.objects.all()
    return render(request, 'school/home.html', {'students': student_data})
