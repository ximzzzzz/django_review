from django.shortcuts import render
import random
# Create your views here.

def index(request):
    return render(request, 'index.html')

def whoami(request):
    return render(request, 'whoami.html')