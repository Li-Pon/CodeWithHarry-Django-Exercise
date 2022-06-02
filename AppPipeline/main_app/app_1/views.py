from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'app_1/index.html')

def app_1_1(request):
    return HttpResponse("app_1_1")

def app_1_2(request):
    return HttpResponse("app_1_2")

def app_1_3(request):
    return HttpResponse("app_1_3")

def app_1_4(request):
    return HttpResponse("app_1_4")
