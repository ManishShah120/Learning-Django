from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse

# Create your views here.
def home(request):
    print("I am Home View")
    return HttpResponse("This is Home Page")

def excp(request):
    print("I am Excp View")
    a = 10/0
    return HttpResponse("This is Excp Page")

def user_info(request):
    print("I am User Info View")
    context = {
        'name': 'Rahul'
    }
    return TemplateResponse(request, 'blog/user.html', context)
