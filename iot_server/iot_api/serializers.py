from rest_framework import serializers
from data.models import Data


class Dataserializer(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = ('id','humidity', 'temp', 'create_data','tozih',)