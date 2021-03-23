from django.http import HttpResponse
from . import randomfor
from django.shortcuts import render
from .models import myDb


def home(request):
    all_items=myDb.objects.all()
    return render(request,'index.html',{'all_items':all_items})

def about(request):
    return HttpResponse("This is about page")

def contact(request):
    return render(request,'contact.html')

def result(request):
    s=request.GET['systolic']
    d = request.GET['diastolic']
    prediction= randomfor.calculatebp(s,d)
    entry = myDb(syst=s,diast=d,pred=prediction)
    entry.save()
    return render(request,'result.html',{'prediction':prediction})