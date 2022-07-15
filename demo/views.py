from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
def login(request):
    return render(request,"login.html")
def home(request):
    email = request.GET["name"]
    pas = request.GET["pass"]
    if(email == "26rishabh10@gmail.com" and pas == 1234):
        return render(request, "home.html")
    else:
        return HttpResponse("Wrong details!!")
             
