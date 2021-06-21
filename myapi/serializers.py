from rest_framework import serializers

from .models import Input

class InputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Input
        fields = ('name', 'message')

        
