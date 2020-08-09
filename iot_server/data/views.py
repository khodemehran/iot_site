from django.shortcuts import render
from django.http import HttpResponse
from .models import Data
from django.utils import timezone

def home(request):
    all_data = Data.objects.order_by('-date')
    return render(request, 'data/home.html',{'all_data':all_data})



def add_data(request):
    if request.method == 'POST':
        if request.POST['humidity'] and request.POST['temp']:
            data = Data()
            data.humidity = request.POST['humidity']
            data.temp = request.POST['temp']
            data.tozih = request.POST['tozih']
            data.date = timezone.datetime.now()
            data.save()
            return render(request,'data/home.html')
    else:
        return render(request, 'data/add_data.html')

        
        