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
    finalans=0
    try:
        if request.method == "GET":
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

def form(request):
    data = {}  

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        service = request.POST.get("service")
        message = request.POST.get("message")

        print(name, email, phone, service, message)

        data = {                     #Using This data dictionary to pass the key values in the form (e.g.<input type="text" name="name" value="{{ name }}" placeholder="Your Name"> )
                                     #to store the previous input data in the form.
            "name": name,
            "email": email,
            "phone": phone,
            "service": service,
            "message": message
        }

    return render(request, "form.html", data)