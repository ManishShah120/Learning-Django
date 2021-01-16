from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def showformdata(request):
    fm = StudentRegistration(auto_id=True, label_suffix='-', initial={'name': 'Sonam', 'email':'manish@gmail.com'})
    return render(request, 'enroll/userregistration.html', {'form':fm})
