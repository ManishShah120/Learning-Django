from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_django(request):
    return HttpResponse('<h1>Hello Django</h1>')

def learn_python(request):
    return HttpResponse('<h1>Hello Python</h1>')

def learn_var(Request):
    a = '<h1>Hello Variable</h1>'
    return HttpResponse(a)

def learn_math(request):
    a = 10+1
    return HttpResponse(a)

def learn_format(request):
    a = 'GeekyShows'
    return HttpResponse(f'Hello, How are you {a}')
