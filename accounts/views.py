from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Your account has been created.")
            login(request, user)
            return redirect("store:product_list")
    else:
        form = SignUpForm()
    return render(request, "accounts/signup.html", {"form": form})

class SignInView(LoginView):
    template_name = "accounts/login.html"

class SignOutView(LogoutView):
    pass

@login_required
def profile(request):
    return render(request, "accounts/profile.html")
