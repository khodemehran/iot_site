from django.shortcuts import render
from django.contrib.auth import get_user_model 
from rest_framework import viewsets
from data.models import Data
from .serializers import Dataserializer,UserSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class DataViewSet(viewsets.ModelViewSet): 
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Data.objects.all()
    serializer_class = Dataserializer


class UserViewSet(viewsets.ModelViewSet): 
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


