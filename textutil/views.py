# Author- vamsi
from django.http import HttpResponse
from django.shortcuts import render
import string
def index(request):
    return render(request,'index.html')
    #return HttpResponse('''<h1>hello<h1> <a href = "https://www.youtube.com/watch?v=9EAM_hlDFko&t=9s"> My Channel </a>''')


def about(request):
    return HttpResponse("About me")
def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc =  request.GET.get('removepunc','off')
    outtext="No analysis"
    if removepunc == 'on':
        outtext=rempunc(djtext)
    params={'purpose':'without Punctuations','analyzed_text':outtext}
    return render(request,'analyze.html',params)

def rempunc(strs):
    analyzed = " "
    for char in strs:
        if char not in string.punctuation:
            analyzed = analyzed + char
        else:
            analyzed=analyzed+" "
    return analyzed
