from django.shortcuts import render
'''from django.http import HttpResponse'''
from rest_framework import generics
from data.models import Data
from .serializers import Dataserializer
# Create your views here.
class List_Data(generics.ListAPIView):

    queryset = Data.objects.all()
    serializer_class = Dataserializer


class Detail_Data(generics.RetrieveAPIView):
    
    queryset = Data.objects.all()
    serializer_class = Dataserializer







