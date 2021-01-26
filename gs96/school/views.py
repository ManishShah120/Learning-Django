from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Q

def home(request):
    student_data = Student.objects.all()

    # student_data = Student.objects.filter(marks=70)
    
    # student_data = Student.objects.exclude(marks=70)
    
    # student_data = Student.objects.order_by('?') # '?[for random]', 'name', 'roll', ''marks
    # student_data = Student.objects.order_by('marks') # '?[for random]', 'name', 'roll', ''marks
    # student_data = Student.objects.order_by('-name') # '?[for random]', 'name', 'roll', ''marks

    # student_data = Student.objects.order_by('id').reverse()

    # student_data = Student.objects.values() # With this the value of the objects gets returned
    # student_data = Student.objects.values('name', 'city')


    # student_data = Student.objects.values_list()
    # student_data = Student.objects.values_list('name', 'city')
    # student_data = Student.objects.values_list('id', 'name', named=True)

    # student_data = Student.objects.using('default')

    # student_data = Student.objects.dates('pass_date', 'year')

    # ######################## Second Tables 'Teacher' Started ########################
    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = qs2.union(qs1)

    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = qs2.union(qs1, all=True)

    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = qs2.intersection(qs1)

    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = qs2.difference(qs1)

    # ######################## AND OR operator ########################
    # student_data = Student.objects.filter(id=6) & Student.objects.filter(roll=106)
    # student_data = Student.objects.filter(id=6, roll=106)
    # student_data = Student.objects.filter(Q(id=6) & Q(roll=106))

    # student_data = Student.objects.filter(id=6) | Student.objects.filter(roll=107)
    # student_data = Student.objects.filter(Q(id=6) | Q(roll=107))

    print("Return: ", student_data)
    print("SQL Query: ", student_data.query) # To get the respected sql query
    return render(request, 'school/home.html', {'students': student_data})
