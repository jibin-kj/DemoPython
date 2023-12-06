from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#first section
"""
def demo(request):
    #return HttpResponse("hello world")
    return render(request,"home.html")#for render html page
def about(request):
    return render(request,"about1.html")

def contact(request):
    return HttpResponse("hello am contact")
    
"""
#passing value
# def demo(request):
#     name="india"
#     return render(request,"home.html",{'obj':name})
def demo(request):

    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,'result.html',{'result':res})