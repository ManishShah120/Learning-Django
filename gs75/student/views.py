from django.shortcuts import render, HttpResponse

# View function for session
def setsession(request):
    request.session['name'] = 'Sonam'
    return render(request, 'student/setsession.html')


# View funtion for GET session
def getsession(request):
    if 'name' in request.session:
        name = request.session['name']
        request.session.modified = True
        return render(request, 'student/getsession.html', {'name': name})
    else:
        return HttpResponse("Your sesison has expired")


# View function for Del Session
def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'student/delsession.html')
