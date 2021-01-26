from django.shortcuts import render
from .models import Student

def home(request):
    # student_data = Student.objects.get(name='Rohit')
    # student_data = Student.objects.get(id=1)
    student_data = Student.objects.get(pk=1)

    # student_data = Student.objects.first()
    # student_data = Student.objects.order_by('name').first()

    # student_data = Student.objects.last()

    # student_data = Student.objects.latest('pass_date')

    # student_data = Student.objects.earliest('pass_date')

    # student_data = Student.objects.all()
    # print(student_data.exists())

    # student_data = Student.objects.all()
    # one_data = Student.objects.get(pk=1)
    # print(student_data.filter(pk=one_data.pk).exists())

    # student_data = Student.objects.create(name="Sameer", roll=114, city="Bokaro", marks=60, pass_date='2020-5-4')

    # student_data, created = Student.objects.get_or_create(name="Sabirr", roll=113, city="Bookaro", marks=90, pass_date='2020-6-4')
    
    # student_data = Student.objects.filter(id=12).update(name='Kabir', marks=80)
    # student_data = Student.objects.filter(marks=70).update(city="Pass")

    # student_data = Student.objects.update_or_create(id=13, name="Sabirr	", defaults={'name': 'Kohli'})

    # objs = [
    #     Student(name='Sonal', roll=120, city='Dhanbad', marks=40, pass_date='2020-5-4'),
    #     Student(name='Kunal', roll=121, city='Dumka', marks=50, pass_date='2020-5-7'),
    #     Student(name='Anisa', roll=122, city='Giridih', marks=70, pass_date='2020-5-9')
    # ]
    # student_data = Student.objects.bulk_create(objs)

    # all_student_data = Student.objects.all()
    # for stu in all_student_data:
    #     stu.city = 'BHEL'
    # student_data = Student.objects.bulk_update(all_student_data, ['city'])

    # student_data = Student.objects.in_bulk([1, 2])
    # print(student_data[1].name)
    # student_data = Student.objects.in_bulk([])
    # student_data = Student.objects.in_bulk()

    # student_data = Student.objects.get(pk=13).delete()
    # student_data = Student.objects.filter(marks=50).delete()
    # student_data = Student.objects.all().delete()

    # student_data = Student.objects.all()
    # print(student_data.count())

    print("Return: ", student_data)
    return render(request, 'school/home.html', {'students': student_data})
  