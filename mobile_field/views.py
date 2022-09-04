import random
from django.shortcuts import render,redirect
from email.message import EmailMessage
import ssl
import smtplib
from .models import User

from rest_framework.authentication import SessionAuthentication


def login_system(request):
    return render(request,'mobile_field/login.html')

def sign_up(request):
    otp_system = False
    email = None
    if request.method == "POST":
        fname = request.POST.get("fname","")
        lname = request.POST.get("lname","")
        email = request.POST.get("email","")
        otp = random.randrange(1000,9999)
        email_sender = ''
        email_password = ''
        email_receiver = email
        subject = "One Time Password"
        body = f"""\t Your OTP is {otp} 
        \n
        Please don't share your otp to anyone"""
        em = EmailMessage()
        em['from'] = email_sender
        em['to'] = email_receiver
        em['subject'] = subject
        em.set_content(body)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender,email_receiver,em.as_string())
        otp_system = True
        user = User(first_name = fname,last_name = lname,email = email,otp_field = otp)
        user.save()
    if request.method == "GET":
        otp = request.GET.get('otp','')
        user  = request.user
        print(user)
    return render(request,'mobile_field/signup.html',{"otp_system":otp_system})

def checkotp(request):
    if request.method == "POST":
        otp = request.POST.get('otp','')
        user = request.user
        print(user)
        return redirect("/")
    return redirect("/")
        

def products(request):
    return render(request,'mobile_field/index.html')