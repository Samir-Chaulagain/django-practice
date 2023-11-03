

from base64 import urlsafe_b64decode
from django.conf import settings

from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from . tokens import generate_token
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from readline import get_current_history_length
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




@csrf_protect
def signup(request):
    if request.method == "POST":
        
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
     
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('homepage')
        
     
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('homepage')
        
        
        
        myuser = User.objects.create_user(fname, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.is_active = False
        myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        
        # Welcome Email
        subject = "Welcome to MusicWorld!!"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to Muse rental Hub !! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nSamir"        
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        # Email Address Confirmation Email
        # current_site = get_current_history_length(request)

        # --------error----------
        # readline = readline()  # Create a Readline object
        # current_site = readline.get_current_history_length()
        email_subject = "Confirm your Email @ GFG - Django Login!!"
        message2 = render_to_string('email_confirmation.html',{
            
            'name': myuser.first_name,
            # 'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
        email_subject,
        message2,
        settings.EMAIL_HOST_USER,
        [myuser.email],
        )
        email.fail_silently = True
        email.send()
        
        return redirect('homepage')
        
        
    return render(request, "signup.html")



def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_b64decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('signin')
    else:
        return render(request,'activation_failed.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "index.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('homepage')
    
    return render(request, "signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('homepage')
