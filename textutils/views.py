# This file is made by me
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")
    # return HttpResponse('<h1>hello world Rishabh</h1>')

def analyzer(request):
    djtext=request.GET.get('text','default')
    print(djtext)
    checkbox=request.GET.get('yesorno','yes')
    print(checkbox)
    answer_text=''
    punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if checkbox=="on":
        for tx in djtext:
            if tx not in punctuations:
                answer_text+=tx
    else:
        answer_text="Check the check box"
    # ans=answer_text
    # print(ans)
    param={"analyzed_text": answer_text}
    return render(request, 'analyzer.html', param)


