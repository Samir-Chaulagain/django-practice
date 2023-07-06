from django.shortcuts import render,HttpResponse,redirect
from .models import Post

# Create your views here.

# def home(request,name):
#     # name="albert eintein"
#     return render(request,"index.html",{'name':name})

# def about(request):
#     return render(request,"about.html")
# def contact(request):
#     return render(request,"contact.html")

def index(request):
    posts=Post.objects.all() #ORM
    return render(request,"index.html",{"posts":posts})
def create(request):
    if request.method=='POST':
        title=request.POST["title"]
        description=request.POST["description"]
        newpost=Post.objects.create(title=title,description=description)
        newpost.save()
        
    return render(request,"create.html")
def delete(request,id):
    Post.objects.get(id=id).delete()
    return redirect("homepage")