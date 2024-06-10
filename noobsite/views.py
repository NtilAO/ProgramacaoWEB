from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def nothing_view(request):
    return HttpResponse("")

def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")

def why_view(request):
    return HttpResponse("Olá noob, o que é que estás aqui a fazer?")

def reason_view(request):
    return HttpResponse("Olá noob, eu sei a razão pela qual tu estás aqui!")

def sleep_view(request):
    return HttpResponse("Olá noob.......ZZZzzzzzzzzzz!")