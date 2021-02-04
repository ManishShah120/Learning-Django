from django.shortcuts import render
from .models import Student, ProxyStudent

# Create your views here.
def home(request):
    # student_data = ProxyStudent.students.get_stu_roll_range(103, 106)
    student_data = ProxyStudent.students.all()
    # student_data = Student.objects.all()
    return render(request, 'school/home.html', {'students': student_data})
