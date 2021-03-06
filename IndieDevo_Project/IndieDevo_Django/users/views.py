# users/views.py

from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import CustomUserCreationForm
from django.contrib import messages
from dashboard.views import dashboard

def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully')
            login(request, user)
            return redirect(reverse("dashboard"))
    else:
        form = customUserCreationForm()
    return render(request, 'users/register.html', {'form': form})