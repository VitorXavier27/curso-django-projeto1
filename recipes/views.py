from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render (request,'recipes/home.html')

def contato(request):
    return HttpResponse('CONTATO 2')
    # return HTTP Response

def sobre(request):
    return HttpResponse('SOBRE 2')
    # return HTTP Response
