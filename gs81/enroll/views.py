from django.shortcuts import render
from django.views.decorators.cache import cache_page

# View function for Home Page
@cache_page(30)
def home(request):
    return render(request, 'enroll/course.html')

# View function for contact Page
def contact(request):
    return render(request, 'enroll/contact.html')
