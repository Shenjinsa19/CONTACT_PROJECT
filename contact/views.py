import logging
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.cache import cache
from .tasks import send_contact_email
logger = logging.getLogger(__name__)

# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             message = form.save()

#             send_contact_email.delay(message.name, message.email, message.message)

#             return redirect('contact_success')

#     else:
#         form = ContactForm()

#     return render(request, 'contact/contact_form.html', {
#         'form': form,
#     })



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save()
            send_contact_email.delay(message.name, message.email, message.message)
            return redirect('contact_success')

    else:
        if request.user.is_authenticated:
            
            cached_data = cache.get(f"user_data_{request.user.username}")
            if cached_data:
                form = ContactForm(initial={
                    'name': cached_data.get('name'),
                    'email': cached_data.get('email'),
                })
            else:
    
                form = ContactForm(initial={
                    'name': request.user.username,
                    'email': request.user.email,
                })
        else:
            form = ContactForm()

    return render(request, 'contact/contact_form.html', {
        'form': form,
    })








from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User

# def register_view(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)  # Your custom form inheriting from UserCreationForm
#         if form.is_valid():
#             user = form.save()  # This hashes password automatically
#             login(request, user)
#             return redirect('contact_form')
#     else:
#         form = RegisterForm()
#     return render(request, 'contact/register.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            

            cache.set(f"user_data_{user.id}", {
                'name': user.username,
                'email': user.email,
            }, timeout=30) 

            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'contact/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('contact_form')  
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'contact/login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('login')

def home_view(request):
    return render(request, 'contact/home.html')
