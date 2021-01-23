from django.shortcuts import render

# View function for session
def setsession(request):
    request.session['name'] = 'Sonam'
    request.session['lname'] = 'Jha'
    return render(request, 'student/setsession.html')


# View funtion for GET session
def getsession(request):
    name = request.session.get('name', default='Guest')
    # To pass the keys to the tempate in a context form
    keys = request.session.keys()
    # We can also get the keys in this way
    items = request.session.items()
    # age = request.session.setdefault('age', '26')
    return render(request, 'student/getsession.html', {'name': name, 'keys': keys, 'items': items})


# View function for Del Session
def delsession(request):
    request.session.flush()
    return render(request, 'student/delsession.html')
