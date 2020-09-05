from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Data
from django.utils import timezone
from django.db.models import Avg

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

    return render(request, 'data/home.html',context)



def add_data(request):
    if request.method == 'POST':
        if request.POST['humidity'] and request.POST['temp']:
            data = Data()
            data.humidity = request.POST['humidity']
            data.temp = request.POST['temp']
            data.tozih = request.POST['tozih']
            #data.create_date = timezone.datetime.now()
            if int(request.POST['humidity']) <= 10:
                print('Warning water shortage!')
            elif int(request.POST['humidity']) >= 100:
                print('I am full of water plz stop doing this any more!')
            else:
                print('humidity:',request.POST['humidity'],'','and its ok!')
            if int(request.POST['temp']) <= 10:
                print('too cold!')
            elif int(request.POST['temp']) >= 100:
                print('too hot here!')
            else:
                print('Temp is:',request.POST['temp'],'','and its ok!')
            print(type(request.POST['humidity']),type(request.POST['temp']))

            data.save()
            return redirect('home')
    else:
        return render(request, 'data/add_data.html')

        
