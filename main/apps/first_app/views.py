from django.shortcuts import render, redirect, HttpResponse
from models import *

def dashboard(request):
    return render(request, 'first_app/dashboard.html')

def register_process(request):
    if request.method == 'POST':
        errors = User.objects.validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            hash1= bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            user = User(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = hash1)
            user.save()
            request.session['id'] = user.id
            request.session['name'] = user.first_name 
            messages.success(request, "Registration was successful")
            return redirect('/login')

def login_process(request):
    if request.method == 'POST':
        errors = User.objects.login_validation(request.POST)   
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)    
            return redirect('/')
        email = request.POST['email']
        user = User.objects.get(email = email)
        request.session['id'] = User.objects.get(email = email).id
        request.session['first_name'] = User.objects.get(email = email).first_name
        return redirect('/')

def login(request):
    return render(request, 'first_app/login.html')

def register(request):
    return render(request, 'first_app/register.html')

            




