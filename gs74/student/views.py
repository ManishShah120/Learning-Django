from django.shortcuts import render

# View function for session
def setsession(request):
    request.session['name'] = 'Sonam'
    return render(request, 'student/setsession.html')


# View funtion for GET session
def getsession(request):
    name = request.session['name']
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    print(request.session.get_expire_at_browser_close())
    return render(request, 'student/getsession.html', {'name': name})


# View function for Del Session
def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'student/delsession.html')
