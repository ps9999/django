from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html',{'name' : 'abhishek'})

def add(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    result = num1 + num2
    return render(request, 'add_result.html', {'result' : result})