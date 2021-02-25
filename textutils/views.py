# This file is made by me
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params={"name":"Rishahh", "place":"India"}
    return render(request,"index.html",params)
    # return HttpResponse('<h1>hello world Rishabh</h1>')

def about(request):
    return HttpResponse("hi world Rishabh")

def one(request):
    with open('one.txt','r') as rf:
        f = rf.read()
        return HttpResponse(f)

def dcwh(request):
    return HttpResponse('<a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7" target="_blank"> django Code with harry </a> ')
def GFG(request):
    return HttpResponse('<a href="https://www.google.com/search?q=geeksforgeeks&oq=geeksforgeeks&aqs=chrome..69i57j0i20i263j69i60l2j69i65l3j69i60.5320j0j4&sourceid=chrome&ie=UTF-8" target="_blank"> GFG </a> ')
def www_dcwh(request):
    return HttpResponse('<a href="https://codewithharry.com/videos/python-django-tutorials-hindi-0" target="_blank">web django Code with harry </a> ')
def oo1_gmail(request):
    return HttpResponse('<a href="https://mail.google.com/mail/u/0/#inbox" target="_blank">001rishabgupta@gmail.com mail box </a> ')
def opti_mail(request):
    return HttpResponse('<a href="https://mail.google.com/mail/u/3/#inbox" target="_blank">opti39rg@gmail.com mail box</a><a href="/"><button typr=button> Click me!</button></a>')

# def back(request):
    # return HttpResponse('<a href="http://127.0.0.1:8000/</a> <button typr=button>Click me!</button>')
