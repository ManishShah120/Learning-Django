from django.shortcuts import render
from django.views import View
from .forms import ContactForm
from django.http import HttpResponse

# Function based view
def homefun(request):
    return render(request, 'school/home.html')


# Class based View
class HomeClassView(View):
    def get(self, request):
        return render(request, 'school/home.html')

# ###################################################

def aboutfun(request):
    context = {'msg': "Welcome to Manish's Home page" }
    return render(request, 'school/about.html', context)


class AboutClassView(View):
    def get(self, request):
        context = {'msg': "Welcome to Manish's Home page" }
        return render(request, 'school/about.html', context)

# ###################################################

def contactfun(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse("Thank You!!! Form Submitted")
    else:
        form = ContactForm()
    return render(request, 'school/contact.html', {'form': form})


class ContactClassView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'school/contact.html', {'form': form})
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse("Thank You!!! Form Submitted")

# ###################################################

def newsfun(request, template_name):
    template_name = template_name
    context = {'info': "CBI enquiry WHy I earn Less Mioney"}
    return render(request, template_name, context)


class NewsClassView(View):
    template_name = ''
    def get(self, request):
        context = {'info': "CBI enquiry why I learn Less Money"}
        return render(request, self.template_name, context)
