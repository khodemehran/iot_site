from django.shortcuts import render
from django.http import HttpResponse
from .models import Data

def home(request):
    all_data = Data.objects.order_by('-date')
    return render(request, 'data/home.html',{'all_data':all_data})