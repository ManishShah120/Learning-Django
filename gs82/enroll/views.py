from django.shortcuts import render

# View function for Home Page
def home(request):
    return render(request, 'enroll/course.html')

# View function for contact Page
def contact(request):
    return render(request, 'enroll/contact.html')
