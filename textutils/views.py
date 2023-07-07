# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")

def removepunc(request):
    # get the text
    djtext = request.GET.get('text', 'default')
    print(djtext)
    # analyze the text
    return HttpResponse("removepunc")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("newline remove first")


def spaceremove(request):
    return HttpResponse("space remover back")

def charcount(request):
    return HttpResponse("charcount ")
