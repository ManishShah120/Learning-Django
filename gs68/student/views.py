from django.shortcuts import render
from datetime import datetime, timedelta

# View function for Setcokie
def setcookie(request):
    response = render(request, 'student/setcookie.html')
    response.set_cookie('name', 'Manish', expires=datetime.utcnow()+timedelta(days=2))
    return response


# Get Cookie Function
def getcookie(request):
    # First way to get the value of the cookie
    # name = request.COOKIES['name']
    # return render(request, 'student/getcookie.html', {'name': name})

    # Second way to get the value of the cookie
    # name = request.COOKIES.get('name')
    # return render(request, 'student/getcookie.html', {'name': name})

    # TO deal with NULL Values
    name = request.COOKIES.get('name', "Guest")
    return render(request, 'student/getcookie.html', {'name': name})


# To delete the cookie
def delcookie(request):
    response =  render(request, 'student/delcookie.html', {'': ''})
    response.delete_cookie('name')
    return response

