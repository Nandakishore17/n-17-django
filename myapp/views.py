from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def TestFun(request):
    return HttpResponse('nandu project')
  
def TestFun1(request):
    return render(request,'index.html')

def TestFun2(request):
    return render(request,'index.html')
    
def TestFun3(request):
    return render(request,'sample-extnd2.html')

def TestFun4(request):
    return render(request,'student-reg.html')

