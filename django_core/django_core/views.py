from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    data = {
        "title": "Home",
        "heading": "Welcome to Our Landing Page"
    }
    return render(request,"index.html",data)

def aboutUS(request):
    return HttpResponse("Hello")

def course(request):
    return HttpResponse("Hello Django!")

def courseDetails(request,courseid):
    return HttpResponse(courseid)