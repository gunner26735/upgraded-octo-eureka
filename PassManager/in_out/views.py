from django.http import HttpResponseRedirect 
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User,auth

# Create your views here.
def log(request):

    if request.method == 'POST':
        uname = request.POST['username']
        mail = request.POST['email']
        pass1 = request.POST['password']

        user = auth.authenticate(username=uname,email=mail,password=pass1)
        if user != None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid UserName or PAssword")
            return redirect('login_url')

    else:
        return render(request,"index.html")

def reg(request):
    if request.method == 'POST':
        uname = request.POST['username']
        mail = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['cpassword']

        if pass1 == pass2:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'Username Already Taken')
                return redirect('reg_url')

            elif User.objects.filter(email=mail).exists():
                messages.info(request,'Email Already Taken')
                return redirect('reg_url')
            else:
                user = User.objects.create_user(username=uname,password=pass1,email=mail)
                user.save()
                print("User created")
                return redirect('login_url')
        else:
            messages.info(request,'Password does not match')
            return redirect('reg_url')
    else:
        return render(request,"register.html")

def out(request):
    logout(request)
    return redirect("/")