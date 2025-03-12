from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import ContactMessage

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def loginUser(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if(user is not None):
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid credentials, please try again')
            return redirect('login')
    return render(request, 'login.html')

def signUp(request):
    if(request.method == 'POST'):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect('login')  # Redirect to home page after signup
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})
            
def contact(request):
    if request.user.is_anonymous:
        return redirect('login')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
        messages.success(request, 'Your message has been sent successfully')
        return redirect('contact')
    return render(request, 'contact.html')

def userInfo(request):
    return render(request, 'user.html', {"user": request.user})

def logoutUser(request):
    logout(request)
    return redirect('/')