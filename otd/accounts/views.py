from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def first(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('/accounts/first')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('/accounts/first')
            else:
                user = User.objects.create_user(username=username, password=password2, email=email)
                user.save();
                messages.info(request,'User created')
                return redirect('/accounts/first')
                
            
        else:
            messages.info(request,'Password not matching')
            return redirect('/accounts/first')
        return redirect('index')    

    else:    
        return render(request,"first.html")


        

def first(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('elements')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('/accounts/first')
    
    
    else:
        return render(request, 'first.html')
