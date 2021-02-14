from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=request.POST['uname']
        email=request.POST['email']
        password=request.POST['password']


        user =User.objects.create_user(username=uname, password=password,email=email,first_name=fname,last_name=lname)
        user.save();
        print('user created')
        return redirect('/')


    else:

        return render(request,'register.html')