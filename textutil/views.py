# Author- vamsi
from django.http import HttpResponse
from django.shortcuts import render
import string


#index method which is the face of the website
def index(request):
    return render(request,'index.html')# Takes request from he index.html template
    #return HttpResponse('''<h1>hello<h1> <a href = "https://www.youtube.com/watch?v=9EAM_hlDFko&t=9s"> My Channel </a>''')

# About page
def about(request):
    return HttpResponse("About me")
#Analyze method which uses the analyze html and return rendered output of the response
def analyze(request):
    djtext = request.GET.get('text','default') #Input text from the website
    removepunc =  request.GET.get('removepunc','off')# remove puncuation flag
    capitalize = request.GET.get('full capital','off')# Capitalize flag
    if removepunc == 'on':
        djtext=rempunc(djtext)# calling the function
    if capitalize == "on":
        djtext = djtext.upper()# capitalizing the input text
    outtext=djtext
    params={'purpose':'','analyzed_text':outtext}# dictionary for render method
    return render(request,'analyze.html',params)

def rempunc(strs):
    '''
    Method for removing puncuations from the text
    Input: string
    returns: string without puncuation
    '''

    analyzed = " "# initializing a parameter
    for char in strs:
        if char not in string.punctuation:
            analyzed = analyzed + char
        else:
            analyzed=analyzed+" "
    return analyzed
