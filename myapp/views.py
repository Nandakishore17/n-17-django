from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def TestFun(request):
    return HttpResponse('hiiiiiii')
  
def TestFun1(request):
    return render(request,'index.html')