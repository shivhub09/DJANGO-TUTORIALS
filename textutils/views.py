# i have created this file - Shivam
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello Harry</h1>")


def about(request):
    return HttpResponse("about Harry")