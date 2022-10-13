import email
from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.http import HttpResponse

from django.contrib.auth.models import User # USer regis ke liye

from django.contrib import messages

from django.contrib.auth import logout

from django.contrib.auth import authenticate, login
# Create your views here.


def homepage(request):
    return render(request, "authen/homepage.html")

def signup(request):
    
    if request.method == "POST":
        username= request.POST["username"] #name attribute wala
        fname= request.POST["fname"]
        lname= request.POST["lname"]
        email= request.POST["email"]
        pass1= request.POST["pass1"]
        pass2= request.POST["pass2"]

        myuser = User.objects.create_user(username,email, pass1)
        myuser.firstname=fname
        myuser.lastname=lname

        

        myuser.save()

        messages.success(request,"Your account has been successfully created!!")

        return redirect("signin")

    


    return render(request, 'authen/signup.html')

def signin(request):

    if request.method =="POST":
        username = request.POST["username"]
        pass1= request.POST["pass1"]

        myuser = authenticate(username=username, password=pass1)  # check ki entered value matches or not

        if myuser is not None:
            login(request, myuser) 

            fname= myuser.first_name
            lname= myuser.last_name

            return render(request,"authen/homepage.html",{'fname':fname,'lname':lname})   
        
        else:
            messages.error(request, "The given credentials dont match!!")
            redirect("homepage")







    return render(request, 'authen/signin.html')

def signout(request):
    logout(request)
    return redirect('homepage')