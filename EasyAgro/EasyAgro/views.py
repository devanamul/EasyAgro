from django.shortcuts import render

def home(request):
	return render(request, "EasyAgro/home.html")

def signin(request):
	return render(request, "EasyAgro/login.html")

def dashboard(request):
	return render(request, "EasyAgro/dashboard.html")