# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")

def analyze(request):
    # get the text
    djtext = request.GET.get('text', 'default')
    print(djtext)
    removepunc = request.GET.get('removepunc', 'default')
    print(removepunc)
    # analyze the text
    analyzed_text = djtext
    punctuations = '''.,?!:;()[]}{<>-—_/'"|@#$%^&*+=~'''
    analyzed = ''
    for char in djtext:
        if char not in punctuations:
            analyzed = analyzed + char
    # return HttpResponse("removepunc")
    params = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
    return render(request, 'analyze.html', params)

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("newline remove first")


# def spaceremove(request):
#     return HttpResponse("space remover back")

# def charcount(request):
#     return HttpResponse("charcount ")
