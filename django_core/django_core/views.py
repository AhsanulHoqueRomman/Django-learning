from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    data = {
        "title": "Home",
        "heading": "Welcome to Our Landing Page",
        "clist": ["Python","Java","Django"],
        "numbers": [10,20,30,40,50,60,70,80],
        "student_details": [
            {"name":"Romman", "Contact": 12345678},
            {"name":"Ahsanul", "Contact": 987654321}
        ]
    }
    return render(request,"index.html",data)

def aboutUS(request):
    return HttpResponse("Hello")

def course(request):
    return HttpResponse("Hello Django!")

def courseDetails(request,courseid):
    return HttpResponse(courseid)