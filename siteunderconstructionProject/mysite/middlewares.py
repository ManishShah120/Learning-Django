from django.shortcuts import HttpResponse, render

class UnderConstructionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
 
    def __call__(self, request):
        print("Call From Middleware Before View")
        # response = self.get_response(request)
        # response = HttpResponse("This is Under Construction.")
        response = render(request, 'mysite/siteuc.html')
        print("Call From Middleware After View")
        return response
