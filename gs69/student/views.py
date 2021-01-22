from django.shortcuts import render
from datetime import datetime, timedelta

# View function for Setcokie
def setcookie(request):
    response = render(request, 'student/setcookie.html')
    response.set_signed_cookie('name', 'Manish', salt='nm', expires=datetime.utcnow()+timedelta(days=2))
    return response


# Get Cookie Function
def getcookie(request):
    name = request.get_signed_cookie('name', default="Guest", salt='nm')
    return render(request, 'student/getcookie.html', {'name': name})


# To delete the cookie
def delcookie(request):
    response =  render(request, 'student/delcookie.html', {'': ''})
    response.delete_cookie('name')
    return response
