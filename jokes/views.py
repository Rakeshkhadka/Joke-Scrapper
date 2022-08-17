from multiprocessing import context
from urllib import response
from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    
    return render(request, 'index.html')
