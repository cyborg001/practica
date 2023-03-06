from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hola(request,name):
    return HttpResponse("hola mundo klk")