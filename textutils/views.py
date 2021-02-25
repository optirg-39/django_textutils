# This file is made by me
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>hello world Rishabh</h1>')

def about(request):
    return HttpResponse("hi world Rishabh")

def one(request):
    with open('one.txt','r') as rf:
        f = rf.read()
        return HttpResponse(f)
