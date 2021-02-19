from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']        
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)  
        if user is not None:
            # messages.info(request, 'logged in successfully')
            return redirect('/')
        else:
            messages.info(request, 'invalid creds')
            return redirect('login')
    else:
        return render(request, "login.html")

def register(request):
    
    if request.method == 'POST':
        firstname = request.POST['firstname']        
        lastname = request.POST['lastname']        
        email = request.POST['email']        
        username = request.POST['username']        
        pass1 = request.POST['pass1']        
        pass2 = request.POST['pass2']
        datas = [username, firstname, lastname, email, pass1, pass2]
        messages.info(request, datas)         
        # return render(request, 'register.html', {'datas' : datas})
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'\n User exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'\n Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email = email, password = pass1, first_name = firstname, last_name = lastname)
                user.save()
                messages.info(request, 'Registered successfully')
                return redirect('login')
        else:
            messages.info(request,'\n Passwords do not match')
            return redirect('register')

        return redirect('/')
    else:
        return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')