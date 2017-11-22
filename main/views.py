from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
# Create your views here.

#from .models import comment

def home(request):
    return render(request, 'home.html', {})