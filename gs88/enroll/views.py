from django.shortcuts import render
from django.core.cache import cache

# View function for Home Page
# def home(request):
#     mv = cache.get('movie', 'has_expired')
#     if mv == 'has_expired':
#         cache.set('movie', 'Theone', 30)
#         mv = cache.get('movie')
#     return render(request, 'enroll/course.html', {'fm': mv})


# def home(request):
#     mv = cache.get_or_set('fees', 200, 30, version=2)
#     return render(request, 'enroll/course.html', {'fm': mv})


# def home(request):
#     data = {
#         'name': 'Sonam',
#         'roll': 101
#     }
#     # cache.set_many(data, 30)
#     sv = cache.get_many(data)
#     print(sv)
#     return render(request, 'enroll/course.html', {'stu': sv})

# def home(request):
#     cache.delete('roll')
#     return render(request, 'enroll/course.html')


# def home(request):
#     # cache.set('roll', 101, 600)
#     # rv = cache.get('roll')
#     rv = cache.decr('roll', delta=3)
#     print(rv)
#     return render(request, 'enroll/course.html')

# def home(request):
#     cache.clear()
#     return render(request, 'enroll/course.html')