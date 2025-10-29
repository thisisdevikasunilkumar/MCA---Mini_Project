from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm

def login_register_view(request):
    if request.method == 'POST':
        if 'register' in request.POST:
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('dashboard')
        elif 'login' in request.POST:
            form = LoginForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('dashboard')
    else:
        form = RegisterForm()
        login_form = LoginForm()

    return render(request, "Login_RegistrationForm.html", {
        'register_form': RegisterForm(),
        'login_form': LoginForm(),
    })


def dashboard(request):
    return render(request, "dashboard.html")
