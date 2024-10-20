from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')
def login(request):
    return render(request, 'Login.html')
def signup(request):
    return render(request, 'Signup.html')