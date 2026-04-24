from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import UsersForm
from services.models import Service
from news.models import News


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
    newsData= News.objects.all() 
    data = {
        'newsData': newsData
    }
    return render(request,"index.html",data)

def aboutUS(request):
    return render(request,"aboutus.html")

def news(request,id):
    newsDetails = News.objects.get(id = id )
    data ={
        'newsDetails': newsDetails
    }
    return render(request,"news.html",data)

def contact(request):
    return render(request,"contact.html")

# def courseDetails(request,courseid):
#     return HttpResponse(courseid)

def services(request):
    serviceData = Service.objects.all().order_by('-name')[1:4]  #order by function used to order ascending or descending.with - it will be order by descending.
                                                               #[x:y] is a syntax of list slicimg which is used for limiting query results that means limiting the object from models from x to y where index started from 0.
    return render(request,"services.html",{
        "services":serviceData
    })

# def calculations(request):
#     finalans=0
#     try:
#         if request.method == "GET":
#         #One method to get the data from the form in GET method
#         # n1= int(request.GET["name"])
#         # n2= int(request.GET["phone"])
#         # print(n1+n2)
#         #Another method is:
#             n1 = int(request.GET.get("name"))
#             n2 = int(request.GET.get("phone"))
#             finalans= n1+n2
#             data = {     
#                 "form" : fn,
#                 "output" : finalans

#             }
#     except:
#         pass
#     return render(request,"calculations.html",{'output':finalans})

def calculations(request):
    fn = UsersForm()
    data = {'form': fn}  
    finalans=0
    try:
        if request.method == "POST":
        #One method to get the data from the form in GET method
        # n1= int(request.GET["name"])
        # n2= int(request.GET["phone"])
        # print(n1+n2)
        #Another method is:
            n1 = int(request.POST.get("number1"))
            n2 = int(request.POST.get("number2"))
            finalans= n1+n2
            data = {     
                "form" : fn,
                "output" : finalans

            }
    except:
        pass
    return render(request,"calculations.html", data)

def form(request):
    
    data = {}  

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        service = request.POST.get("service")
        message = request.POST.get("message")

        print(name, email, phone, service, message)
        #Using This data dictionary to pass the key values in the form (e.g.<input type="text" name="name" value="{{ name }}" placeholder="Your Name"> )
        #to store the previous input data in the form in case we want to store the submitted data in the form and there is no redirect page.
        data = {                  
            "name": name,
            "email": email,
            "phone": phone,
            "service": service,
            "message": message
        }

        
        return redirect('/thank/')          #we can use the HTTPResponseRedirect which also does the same job.

    return render(request, "form.html", data)

def thank(request):
            return render(request,"thank.html")

def submitform(request):
    finalans=0
    try:
        if request.method == "GET":
        
        #Another method is:
            n1 = int(request.GET.get("name"))
            n2 = int(request.GET.get("phone"))
            finalans= n1+n2

            return HttpResponse(finalans)
    except:
        pass

def calculator(request):
     result=""
     try:
          if request.method == "POST":
               n1=eval(request.POST.get("num1"))
               opr= request.POST.get("operator")
               n2=eval(request.POST.get("num2"))
               if opr== "add":
                    result = n1+n2
               elif opr == "sub":
                    result = n1-n2
               elif opr == "mul":
                    result = n1*n2
               elif opr == "div":
                    result = n1/n2

                    

     except:
          result = "Invalid User Input"         

     return render(request, "calculator.html",{"result":result})
    
    #We are using action method to show the form data on required url. We can use this method with POST method also.
    #By using action we can show the data whatever the url we want.And we can use redirect ar HTTPResponse to show the form data.

def evenodd(request):
     result = ''
     if request.method =="POST":
          if request.POST.get('number') == "":
              return render(request, "evenodd.html", {'error': True})
          
          n = int(request.POST.get('number'))
          if n%2 ==0:
               result = "Even Number"
          else:
               result = "Odd Number"

     return render(request,"evenodd.html", {'result': result })
    
def marksheet(request):
     totalnum = ''
     percentage = ''
     grade = ''

     if request.method =="POST":
          n1 = eval(request.POST.get('mark1'))
          n2 = eval(request.POST.get('mark2'))
          n3 = eval(request.POST.get('mark3'))
          n4 = eval(request.POST.get('mark4'))
          n5 = eval(request.POST.get('mark5')) 

          totalnum = n1 + n2 + n3 + n4 + n5
          percentage = (totalnum / 500) * 100

          if percentage >= 80:
            grade = 'A+'
          elif percentage >= 70:
            grade = 'A'
          elif percentage >= 60:
            grade = 'B'
          elif percentage >= 50:
            grade = 'C'
          elif percentage >= 40:
            grade = 'D'
          else:
            grade = 'Fail'

          return render(request,"marksheet.html", {
         'totalnum' : totalnum,
         'percentage' : percentage,
         'grade' : grade
     })

     return render(request,"marksheet.html")