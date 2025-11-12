from django.shortcuts import render

def main_page(request):
    return render(request, 'Main Page.html')

def login_register(request):
    return render(request, 'Login Registration Form.html')
