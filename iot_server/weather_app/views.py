from django.shortcuts import render

# Create your views here.
def weather(request):
    return render(request,'weather_app/index.html')