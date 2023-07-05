from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('hello guys')

def secondhome(request):
    return HttpResponse('hello good people')