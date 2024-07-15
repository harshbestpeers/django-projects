from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('board')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


