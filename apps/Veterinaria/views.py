from django.shortcuts import render
from .admin import *

# Create your views here.

def index(request):
    allproduct = animales.objects.all()
    return render(request, 'index.html', {'AnimalesStock':allproduct})