from django.shortcuts import render
from .models import user
from django.views.generic.edit import CreateView
# Create your views here.

class GeeksCreate(CreateView):
    model = user
    fields = ["first_name", "last_name", "email", "password"]