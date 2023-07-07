# i have created this file - Shivam
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'harry', 'place':"Mars"}
    return render(request, 'index.html', params)


def removepunc():
    return HttpResponse("remove punc")

def capfirst():
    return HttpResponse("capitalize")

def lineremove():
    return HttpResponse("remove an extra line   ")

def spaceremove():
    return HttpResponse("remove an space   ")

def charcount():
    return HttpResponse("count the number of characters   ")