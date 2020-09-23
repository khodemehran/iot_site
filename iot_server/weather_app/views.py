from django.shortcuts import render,get_object_or_404,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
import requests
from .models import City
from .forms import CityForm
@login_required
def index(request):
    api_key='60cf1c6da2b4a138ed138d16217ac674'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'

    err_msg = ''
    message = ''
    message_class = ''

    cities = City.objects.all()
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name__iexact=new_city).count()
            if existing_city_count == 0:
                r = requests.get(url.format(new_city,api_key)).json()
                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'City Not Found'
            else:
                err_msg = 'City Has Already Exist In Database'
        
        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = 'City added successfully!'
            message_class = 'is-success'

    print(err_msg)

    form = CityForm()
    weather_data = []
    for city in cities:

        city_weather = requests.get(url.format(city,api_key)).json()
        print(city_weather)

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather)

    context = {'weather_data' : weather_data,
    'form' : form,
    'message': message,
    'message_class': message_class,
    }



    return render(request, 'weather_app/weather.html',context)

@login_required
def delete_city(request,city_name):

    City.objects.get(name=city_name).delete()
    return redirect("weather")

