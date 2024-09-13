from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if User.objects.filter(username=username):
            messages.error(request, "cd nom d'utilisateur existe déjà")
            return redirect('register')
        if User.objects.filter(email=email):
            messages.error(request, "cet email est déjà utilisteur")
            return redirect('register')
        if not username.isalnum():
            messages.error(request, "le nom doit etre alpha numerique") 
            return redirect('register')
        
        if password != password1:
            messages.error(request, " les mot de passe ne correspondent pas") 
            return redirect('register')

        my_user = User.objects.create_user(username, email, password)
        my_user.first_name = firstname
        my_user.last_name = lastname
        my_user.save()  
        messages.success(request, 'votre compte a été créé success')

        return redirect('login',)


    return render(request, 'authentication/register.html')

def logIn(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list_articles')
        else:
            messages.error(request, 'Mauvaise authentification')
            return redirect('login')
    return render(request, 'authentication/login.html')

def logOut(request):
    logout(request)
    messages.success(request, 'Vous avez été bien deconnecté')
    return redirect('login')
