from django.shortcuts import render
from .models import Student
from datetime import date, time


def home(request):
    student_data = Student.objects.all()
    # student_data = Student.objects.filter(name__exact='Sonam')
    # student_data = Student.objects.filter(name__iexact='sonam')
    # student_data = Student.objects.filter(name__contains='U')
    # student_data = Student.objects.filter(id__in=[1, 5, 7])
    # student_data = Student.objects.filter(marks__in=[60, 70])
    # student_data = Student.objects.filter(marks__gt=60)
    # student_data = Student.objects.filter(marks__gte=60)
    # student_data = Student.objects.filter(marks__lt=60)
    # student_data = Student.objects.filter(marks__lte=60)
    # student_data = Student.objects.filter(name__startswith='S')
    # student_data = Student.objects.filter(name__istartswith='s')
    # student_data = Student.objects.filter(name__endswith='i')
    # student_data = Student.objects.filter(name__iendswith='I')
    # student_data = Student.objects.filter(passdate__range=('2019-01-01', '2021-01-01'))
    # student_data = Student.objects.filter(admdatetime__date=date(2020,7,10))
    # student_data = Student.objects.filter(admdatetime__date__gt=date(2020,7,10))
    # student_data = Student.objects.filter(passdate__year=2020)
    # student_data = Student.objects.filter(passdate__year__gte=2020)
    # student_data = Student.objects.filter(passdate__month=1)
    # student_data = Student.objects.filter(passdate__month__gt=10)
    # student_data = Student.objects.filter(passdate__day=24)
    # student_data = Student.objects.filter(passdate__week=14)
    # student_data = Student.objects.filter(passdate__week_gt=14)
    # student_data = Student.objects.filter(passdate__week__day=5)
    # student_data = Student.objects.filter(passdate__week__day__gt=5)
    # student_data = Student.objects.filter(passdate__quarter=2)
    # student_data = Student.objects.filter(admdatetime__time__gt=time(6, 00))
    # student_data = Student.objects.filter(admdatetime__hour__gt=5)
    # student_data = Student.objects.filter(admdatetime__minute__gt=20)
    # student_data = Student.objects.filter(admdatetime__second__gt=20)
    # student_data = Student.objects.filter(roll__isnull=False)

    print("Return: ", student_data)
    stu_query = student_data.query
    return render(request, 'school/home.html', {'students': student_data, 'stu_query': stu_query})
