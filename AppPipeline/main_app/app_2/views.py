from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'app_2/index.html')

def app_2_1(request):
    return HttpResponse("app_2_1")

def app_2_2(request):
    return HttpResponse("app_2_2")

def app_2_3(request):
    return HttpResponse("app_2_3")

def app_2_4(request):
    return HttpResponse("app_2_4")