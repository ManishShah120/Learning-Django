from django.shortcuts import render
from datetime import datetime

# Create your views here.
def learn_django(request):
    # django_details = {
    #     'cname': 'django is Awesome',
    #     'duration': '4 Months',
    #     'seats': 10
    #     }
    # return render(request, 'course/courseone.html', context = django_details) # context only takes dictionary type
    ## Example no. 4
    # d = datetime.now()
    # return render(request, 'course/courseone.html', context = {'dt': d})
    ## Example no. 5
    # return render(request, 'course/courseone.html', context = {
    #     'p1': 56.24321,
    #     'p2':56.0000,
    #     'p3': 56.37000
    # })
    ## Example no. 6
    # return render(request, 'course/courseone.html', context = {
    #     'nm': False
    # })
    ## Example no. 7
    # student = {'names': ['Rahul', 'Moitaliy', 'Frinhwe', 'Tiqpao', 'Xaeoqzt']}
    # return render(request, 'course/courseone.html', context = student)
    ## Example no. 8
    # stu = {
    #     'stu1': {'name': 'Rahul', 'roll': 101},
    #     'stu2': {'name': 'Poyuiwa', 'roll': 102},
    #     'stu3': {'name': 'Muidta', 'roll': 103},
    #     'stu4': {'name': 'Puxiqn', 'roll': 104},
    # }
    # students = {
    #     'student': stu
    # }
    # return render(request, 'course/courseone.html', context = students)
    ## Example no. 9
    # data = {
    #     'Name': 'Rahul',
    #     'Roll': 101
    # }
    # return render(request, 'course/courseone.html', context = {'data': data})
    ## Example no. 10
    data = {
        'stu1': {'name': 'Rahul', 'roll': 101},
        'stu2': {'name': 'Poyuiwa', 'roll': 102},
        'stu3': {'name': 'Muidta', 'roll': 103},
        'stu4': {'name': 'Puxiqn', 'roll': 104},
    }
    return render(request, 'course/courseone.html', context = {'data': data})
