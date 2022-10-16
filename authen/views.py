# import csv
from email import message
import smtplib, ssl
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


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

def feedback(request):
    if request.method=='POST':
        username = request.POST["username"]
        email= request.POST["email"]
        journey=request.POST["journey"]

        # msg["To"] = email
        # msg['Subject']="Hi, "+username+" Thank you for Subscription for our BlogPost Services"
        # server= smtplib.SMTP_SSL("smtp.gmail.com",465)
        # server.login("abhaychandra2499@gmail.com", "")  #change email
        # server.send_message(msg)

        port = 465  # For SSL
        password = "pndvybfxbrqymukx"

        sender_email = "abhaychandra2499@gmail.com"  # Enter your address
        receiver_email = email # Enter receiver address

        message = MIMEMultipart("alternative")
        message["Subject"] = "multipart test"
        message["From"] = sender_email
        message["To"] = receiver_email

        html = """\
                    <html>
                    <body>
                        <p>Hi,<br>
                        How are you?<br>
                        
                        <h2>Thank you for expressing your thought to us</h2> <br>
                        We have received your input and assigned our special professional, Dr Sangeeeta Srivastava, to address it
                        Cheers!

                        </p>
                        <br>
                        <br>
                        <b><H4>Dr. Sangeeta Srivastava <br> Phone: 9415404602, 8756941925 <br>Email: sangsri369@gmail.com</p>
                        <!-- <h4>The Response we recieved was: </h4> -->
                    </body>
                    </html>
                """
        
        part1 = MIMEText(html, "html")

        message.attach(part1)
        
        

        # Create a secure SSL context
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        
    return redirect('homepage')

            

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

def doctinfo(request):
    return render(request,'authen/doctinfo.html')



def products3(request):
    return render(request,'authen/products3.html')

def relax(request):
    return render(request,'authen/relax.html')

def games(request):
    return render(request,'authen/games.html')


def fruitninga(request):
    return render(request,'authen/fruitninga.html')

def colorblast(request):
    return render(request,'authen/colorblast.html')

def snake(request):
    return render(request,'authen/snake.html')



