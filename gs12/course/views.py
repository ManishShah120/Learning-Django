from django.shortcuts import render

# Create your views here.
def learn_django(request):
    django_details = {
        'cname': 'Django',
        'duration': '4 Months',
        'seats': 10
        }
    return render(request, 'course/courseone.html', context = django_details)

def learn_python(request):
    python_details = {
        'cname': 'Python',
        'duration': '6 Months',
        'seats': 20
        }
    return render(request, 'course/coursetwo.html', python_details)
