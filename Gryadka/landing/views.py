from django.shortcuts import render
from datetime import datetime
#from .forms import *

# Create your views here.
def landing(request):
    return render(request, 'landing\\landing.html')
