from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def register(request):
    return HttpResponse('Hello, World!')
    # return render(request, 'register/register.html')


