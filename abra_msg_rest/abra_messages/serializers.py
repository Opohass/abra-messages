from rest_framework import serializers
from .models import AbraMessages


"""Message Serializer using all fields"""
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbraMessages
        fields = '__all__'


class MessageReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbraMessages
        fields = ['msg_read']
