from django.shortcuts import  render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.forms import AuthenticationForm

from authentication.models import History

def register_request(request):
	if request.method == "POST":
		email = request.POST.get('email')
		username = request.POST.get('name')
		password = request.POST.get('pass')
		password2 = request.POST.get('pass2')
		if User.objects.filter(email=email).exists():
			messages.error(request, "Email already exists.")
			return redirect("authentication:register")
		else:
			if password == password2:
				
				user = User.objects.create(username=username, email=email, password=make_password(password))
				user.save()
				messages.success(request, "Registration successful." )
				return redirect("authentication:login")
			else:
				messages.error(request, "Passwords do not match.")
				return redirect("authentication:register")

	return render (request=request, template_name="authentication/register.html")

def login_request(request):
	if request.method == "POST":
			username = request.POST.get('name')
			password = request.POST.get('pass')
			user = authenticate(username=username, password=password)
			print(user)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("ml_app:home")
			else:
				messages.error(request,"Invalid username or password.")
   
	return render(request=request, template_name="authentication/login.html")

def history(request):
	history = History.objects.filter(user = request.user)
	return render(request, "authentication/history.html", context = {"history" : history });


def logoutUser(request):
	logout(request)
	return redirect('authentication:login')

