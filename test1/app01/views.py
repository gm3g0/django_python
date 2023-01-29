from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("哈囉")


def login(request):
    return render(request, "login.html")


def singup(req):
    return render(req, "singup.html")

def exercise(req):
    return render(req, "exercise.html")

def teaching(req):
    return render(req, "teaching.html")    
