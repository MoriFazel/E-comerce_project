from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def calculate():
    x=1
    y=2
    return x

def say_hello(request):
    #return HttpResponse("Hello, World!")

    x=calculate()
    return render(request, "hello.html", {"name": "Mori"})