from django.shortcuts import render

# View function for session
def setsession(request):
    request.session['name'] = 'Sonam'
    request.session['lname'] = 'Jha'
    return render(request, 'student/setsession.html')

# View funtion for GET session
def getsession(request):
    # First Method
    # name = request.session['name']
    # return render(request, 'student/getsession.html', {'name': name})

    # Second Method to deal with None value or no values
    name = request.session.get('name', default='Guest')
    lname = request.session.get('lname', default='Guest')
    return render(request, 'student/getsession.html', {'name': name, 'lname': lname})

# View function for Del Session
def delsession(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request, 'student/delsession.html')
