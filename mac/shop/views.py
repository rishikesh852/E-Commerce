from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'shop/index.html')


def about(request):
    return render(request, 'shop/about.html')


def Contact(request):
    return HttpResponse("We are at Contact")


def tracker(request):
    return HttpResponse("We are at tracker")


def search(request):
    return HttpResponse("We are at search")


def productview(request):
    return HttpResponse("We are at proView")


def checkout(request):
    return HttpResponse("We are at checkout")
