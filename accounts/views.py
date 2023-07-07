from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_safe, require_POST

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout, get_user_model
from django.contrib.auth.decorators import login_required
# Create your views here.
from . forms import CustomUserCreationForm
from hotel_booking.models import HotelInfo, HotelProduct
from booking.models import Book

User = get_user_model()

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'GET':
        signup_form = CustomUserCreationForm()
    else:
        signup_form = CustomUserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
        
    return render(request, 'accounts/signup.html', {
        'signup_form' : signup_form,
    })

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'GET':
        login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            auth_login(request, user)
            return redirect(request.GET.get('next') or 'home')
        
    return render(request, 'accounts/login.html', {
        'login_form' : login_form,
    })

def logout(request):
    auth_logout(request)
    return redirect('home')

@login_required
@require_http_methods(['GET', 'POST'])
def profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    books = profile_user.books.all()


    return render(request, 'accounts/profile.html', {
        'profile_user' : profile_user,
        'books': books,
    })
