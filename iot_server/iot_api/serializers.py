from django.contrib.auth import get_user_model
from rest_framework import serializers
from data.models import Data


class Dataserializer(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = ('author','id','humidity','temp','tozih','created_at')


class UserSerializer(serializers.ModelSerializer): # new
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)
    