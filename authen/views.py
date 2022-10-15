# import csv
from email import message
import smtplib, ssl
from email.message import EmailMessage

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

        user = User.objects.create_user(username, email, pass1)
        user.first_name=fname
        user.last_name=lname

        

        user.save()

        messages.success(request,"Your account has been successfully created!!")

        return redirect("signin")

    


    return render(request, 'authen/signup.html')

def signin(request):

    if request.method =="POST":
        username = request.POST["username"]
        pass1= request.POST["password"]

        user = authenticate(username=username, password=pass1)  # check ki entered value matches or not

        if user is not None:
            login(request, user)
            fname= user.first_name
            lname= user.last_name
            
            print(fname, lname)                                              #For debug, remove it later
            # messages.success(request, f' welcome {username} !!')
            diction={'fname':fname,'lname':lname}
            return render(request,"authen/homepage.html",diction)   
        
        else:
            messages.error(request, "The given credentials dont match!!")
            redirect("homepage")







    return render(request, 'authen/signin.html')

def signout(request):
    logout(request)
    return redirect('homepage')

# msg=EmailMessage()
# msg.set_content('Hello there!!! \nTHANK YOU FOR SUSCRIBING INTO OUR BLOGPOST!!! \n Check for New blogs at our website!!')
# msg['From']="abhaychandra2499@gmail.com"
# email=""
# username=""

def blogs(request):
    if request.method=='POST':
        username = request.POST["username"]
        email= request.POST["email"]

        # msg["To"] = email
        # msg['Subject']="Hi, "+username+" Thank you for Subscription for our BlogPost Services"
        # server= smtplib.SMTP_SSL("smtp.gmail.com",465)
        # server.login("abhaychandra2499@gmail.com", "")  #change email
        # server.send_message(msg)

        port = 465  # For SSL
        password = "pndvybfxbrqymukx"

        sender_email = "abhaychandra2499@gmail.com"  # Enter your address
        receiver_email = email # Enter receiver address

        msg="Hi, "+username+" Thank you for Subscription for our BlogPost Services"

        # Create a secure SSL context
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg)
            


        
    return render(request,'authen/blogs.html')

# def read_info():
#     with open('susinfo.csv', 'r') as file:
#         reader = csv.reader(file)
#         a=[]
#         for row in reader:
#             a.append(row)
#         useremail=row[-1]
#         return useremail

def about(request):
    return render(request,'authen/about.html')




def todo(request):
    return render(request,'authen/todo.html')



def ventfeels(request):
    return render(request,'authen/ventfeels.html')



def product3(request):
    return render(request,'authen/product3.html')



