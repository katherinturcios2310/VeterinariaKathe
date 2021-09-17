from django.shortcuts import render

# Create your models here.

def index(request):
    return render(request, 'index.html'),