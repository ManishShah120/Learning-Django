from django.shortcuts import render
from .models import Student
from django.db.models import Avg, Sum, Min, Max, Count

def home(request):
    student_data = Student.objects.all()
    average = student_data.aggregate(Avg('marks'))
    sum = student_data.aggregate(Sum('marks'))
    max = student_data.aggregate(Max('marks'))
    min = student_data.aggregate(Min('marks'))
    count = student_data.aggregate(Count('marks'))
    print(average)
    print(sum)
    print(max)
    print(min)
    print(count)

    print("Return: ", student_data)
    stu_query = student_data.query
    return render(request, 'school/home.html', {'students': student_data, 'stu_query': stu_query})
