# This file is made by me
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def analyzer(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('yesorno', 'yes')
    capitalize_first = request.POST.get('capitalize', 'yes')
    newlineremover = request.POST.get('newlineremover', 'yes')
    extraspaceremover = request.POST.get('extraspaceremover', 'yes')
    charcount = request.POST.get('charcount', 'yes')

    punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if removepunc=="on":
        answer_text = ''
        for tx in djtext:
            if tx not in punctuations:
                answer_text+=tx
        djtext=answer_text
        param = {'Purpose': 'Remove Punctuations', "analyzed_text": answer_text}
    if capitalize_first =="on":
        answer_text = ''
        for char in djtext:
            answer_text+=char.upper()
        djtext = answer_text
        param = {'Purpose': 'CAPITALIZE FIRST', "analyzed_text": answer_text}
    if newlineremover =="on":
        answer_text = ''
        for char in djtext:
            if char !="\n" and char !="\r":
                answer_text+=char
        djtext = answer_text
        param = {'Purpose': 'newlineremover', "analyzed_text": answer_text}
    if extraspaceremover =="on":
        answer_text = ''
        for index,char in enumerate(djtext,0):
            if index==(len(djtext)-1):
                pass
            elif not (djtext[index]==" " and djtext[index+1]==" "):
                answer_text+=char
        djtext = answer_text
        param = {'Purpose': 'extraspaceremover', "analyzed_text": answer_text}
    if charcount == "on":
        answer_text = ''
        d={}
        for char in djtext:
            if char in d.keys():
                pass
            else:
                d[char]=djtext.count(char)
        answer_text = d
        param = {'Purpose': 'charcount', "analyzed_text": answer_text}
    if charcount != "on" and extraspaceremover !="on" and newlineremover !="on" and capitalize_first !="on" and removepunc !="on":
        return render(request, 'valid.html')

    return render(request,'analyzer.html', param)


