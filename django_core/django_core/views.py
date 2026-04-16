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

def calculations(request):
    try:
        finalans=0
        #One method to get the data from the form in GET method
        # n1= int(request.GET["name"])
        # n2= int(request.GET["phone"])
        # print(n1+n2)
        #Another method is:
        n1 = int(request.GET.get("name"))
        n2 = int(request.GET.get("phone"))
        finalans= n1+n2
    except:
        pass
    return render(request,"calculations.html",{'output':finalans})