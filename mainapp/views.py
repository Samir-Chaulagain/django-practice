from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request,name):
    # name="albert eintein"
    return render(request,"index.html",{'name':name})

def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")