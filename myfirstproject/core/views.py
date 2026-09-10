# Create your views here.
# Views - A view handles a request and returns a response.

from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')

