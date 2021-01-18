from django.shortcuts import render

# Create your views here.
def show_details(request, year):
    return render(request, 'enroll/show.html', {'yr': year})
