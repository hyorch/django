from django.shortcuts import render
from django.http import HttpResponse

def primera_vista(request):
    return HttpResponse("Hola <b>Django</b> World <br> ¿dónde están los máquinas?")


