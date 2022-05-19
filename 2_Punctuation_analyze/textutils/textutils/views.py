# I have created this file - Li Pon
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text from form
    text_area_text = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    print(text_area_text)
    print(removepunc)
    # analyzed = text_area_text
    punctuations = '''!()-[]}{;:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    for char in text_area_text:
        if removepunc == "on":
            if char not in punctuations:
                analyzed += char
        else:
            analyzed = text_area_text
    params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
    # Analyze the text
    return render(request, 'analyze.html',params)
