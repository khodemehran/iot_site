from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Data
from django.utils import timezone
from django.db.models import Avg

@login_required
def home(request):
    all_data = Data.objects.order_by('-created_at')
    Temp_Avg = Data.objects.aggregate(Avg('temp'))
    Temp_Avg = Temp_Avg["temp__avg"] 
    Humidity_Avg = Data.objects.aggregate(Avg('humidity'))
    Humidity_Avg = Humidity_Avg["humidity__avg"]
    last_pk = all_data.count()
    Last_data = Data.objects.order_by('-id')

    context = {
        'all_data':all_data,
        'Temp_Avg':Temp_Avg,
        'Humidity_Avg':Humidity_Avg,
        'last_pk':last_pk,
        'Last_data':Last_data,
        }

    return render(request, 'data/index.html',context)


@login_required
def add_data(request):
    if request.method == 'POST':
        if request.POST['humidity'] and request.POST['temp']:
            data = Data()
            data.humidity = request.POST['humidity']
            data.temp = request.POST['temp']
            data.tozih = request.POST['tozih']
            data.author = request.user
            #data.create_date = timezone.datetime.now()
            if int(request.POST['humidity']) <= 10:
                humidity_report = print('Warning water shortage!')
            elif int(request.POST['humidity']) >= 100:
                humidity_report = print('I am full of water plz stop doing this any more!')
            else:
                humidity_report = print('humidity:',request.POST['humidity'],'','and its ok!')
            if int(request.POST['temp']) <= 10:
                temp_report = print('too cold!')
            elif int(request.POST['temp']) >= 100:
                temp_report = print('too hot here!')
            else:
                temp_report = print('Temp is:',request.POST['temp'],'','and its ok!')
            print(type(request.POST['humidity']),type(request.POST['temp']))
            context = {
                'humidity_report':humidity_report,
                'temp_report':temp_report,
            }
            data.save()
            return render(request, 'data/index.html', context)
    else:
        return render(request, 'data/add_data.html')

        
