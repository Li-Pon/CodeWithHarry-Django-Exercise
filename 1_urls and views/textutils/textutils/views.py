# I have created this file - Li Pon
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Add These in local server</h1>"
                        "<h2>google</h2>"
                        "<h2>facebook</h2>"
                        "<h2>youtube</h2>")


def google(request):
    return HttpResponse('''<a href="https://www.google.com/">Google</a>''')


def facebook(request):
    return HttpResponse('''<a href="https://www.facebook.com/">Facebook</a>''')


def youtube(request):
    return HttpResponse('''<a href="https://www.youtube.com/">Youtube</a>''')
