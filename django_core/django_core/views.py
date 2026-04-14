from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # data = {
    #     "title": "Home",
    #     "heading": "Welcome to Our Landing Page",
    #     "clist": ["Python","Java","Django"],
    #     "numbers": [10,20,30,40,50,60,70,80],
    #     "student_details": [
    #         {"name":"Romman", "Contact": 12345678},
    #         {"name":"Ahsanul", "Contact": 987654321}
    #     ]
    # }
    return render(request,"index.html")

def aboutUS(request):
    return render(request,"aboutus.html")

def contact(request):
    return render(request,"contact.html")

# def courseDetails(request,courseid):
#     return HttpResponse(courseid)

def services(request):
    return render(request,"services.html")