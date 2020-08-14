#dashboard/views.py
from django.shortcuts import render 
from django.http import HttpResponse 
from users.views import dashboard
# Create your views here.

def dashboard(request):
    return render(request, "users/dashboard.html")
