# This file is made by me
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")
    # return HttpResponse('<h1>hello world Rishabh</h1>')

def analyzer(request):
    djtext = request.GET.get('text','default')
    print(djtext)
    removepunc = request.GET.get('yesorno', 'yes')
    capitalize_first = request.GET.get('capitalize', 'yes')
    newlineremover = request.GET.get('newlineremover', 'yes')
    extraspaceremover = request.GET.get('extraspaceremover', 'yes')
    charcount = request.GET.get('charcount', 'yes')

    answer_text = ''
    print(djtext)

    punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if removepunc=="on":
        for tx in djtext:
            if tx not in punctuations:
                answer_text+=tx
        print(answer_text)
        print(djtext)
        param = {'Purpose': 'Remove Punctuations', "analyzed_text": answer_text}
    elif capitalize_first =="on":
        for char in djtext:
            answer_text+=char.upper()
        print(answer_text)
        param = {'Purpose': 'CAPITALIZE FIRST', "analyzed_text": answer_text}
    elif newlineremover =="on":
        for char in djtext:
            if char !="\n":
                answer_text+=char
        param = {'Purpose': 'newlineremover', "analyzed_text": answer_text}
    elif extraspaceremover =="on":
        for index,char in enumerate(djtext,0):
            if index==(len(djtext)-1):
                pass
            elif not (djtext[index]==" " and djtext[index+1]==" "):
                answer_text+=char
        param = {'Purpose': 'extraspaceremover', "analyzed_text": answer_text}
    elif charcount == "on":
        d={}
        for char in djtext:
            if char in d.keys():
                pass
            else:
                d[char]=djtext.count(char)
        answer_text = d
        param = {'Purpose': 'charcount', "analyzed_text": answer_text}
    else:
        return HttpResponse('Error occur')

    return render(request,'analyzer.html', param)


