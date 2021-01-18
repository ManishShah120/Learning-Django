from django.shortcuts import render

# Create your views here.
## We are using an additional passing parameter
def home(request, check):
    return(render(request, 'enroll/home.html', context={'ch': check}))

# def show_details(request, my_id):
#     return render(request, 'enroll/show.html', {'my_id': my_id})

def show_details(request, my_id=1):
    if my_id == 1:
        student = {'id': my_id, 'name': 'manish'}
    if my_id == 2:
        student = {'id': my_id, 'name': 'Kumar'}
    if my_id == 3:
        student = {'id': my_id, 'name': 'Shah'}
    return render(request, 'enroll/show.html', student)

def show_subdetails(request, my_id, my_subid):
    if my_id == 1 and my_subid == 5:
        student = {'id': my_id, 'name': 'manish', 'info': 'Sub Details'}
    if my_id == 2 and my_subid == 6:
        student = {'id': my_id, 'name': 'Kumar', 'info': 'Sub Details'}
    if my_id == 3 and my_subid == 7:
        student = {'id': my_id, 'name': 'Shah', 'info': 'Sub Details'}
    return render(request, 'enroll/show.html', student)
