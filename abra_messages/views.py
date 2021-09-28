from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import MessageSerializer, MessageReadSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AbraMessages
from rest_framework import status, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


class AbraMessageViewSet(APIView):
    """
    A simple ViewSet for listing or retrieving users.
    """
    permission_classes = [IsAuthenticated]


    def get(self, request, pk=None, format=None):
        if pk:
            abra_message = get_object_or_404(AbraMessages, id=pk)
            abra_serializers = MessageSerializer(abra_message)
            return Response(abra_serializers.data, status=status.HTTP_200_OK)
        else:
            abra_messages_qs = AbraMessages.objects.filter(Q(sender=request.user) | Q(receiver=request.user))
            abra_serializers = MessageSerializer(abra_messages_qs, many=True)
            return Response(abra_serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        abra_serializers = MessageSerializer(data=request.data)
        abra_serializers.is_valid(raise_exception=True)
        abra_serializers.validated_data['sender']=request.user
        abra_serializers.save()
        return Response(abra_serializers.data, status=status.HTTP_201_CREATED)

    def patch(self, request, pk=None, format=None):
        abra_message = get_object_or_404(AbraMessages, id=pk)
        if abra_message.sender != request.user and abra_message.receiver != request.user:
            return Response({'message': 'you cant read another user message'}, status=400)    
        abra_serializers = MessageReadSerializer(instance=abra_message, data=request.data)
        abra_serializers.is_valid(raise_exception=True)
        abra_serializers.save()
        return Response(abra_serializers.data, status=status.HTTP_200_OK)

    def delete(self,request, pk=None, format=None):
        abra_message = get_object_or_404(AbraMessages, id=pk)
        if abra_message.sender == request.user or abra_message.receiver == request.user:
            abra_message.delete()
            return Response({'msg': 'done'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message': 'you can delete only your messasge'}, status=400)    



class AbraMessageUnradViewSet(APIView):
    """
    A simple ViewSet for listing or retrieving users.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, format=None):
        abra_messages_qs = AbraMessages.objects.filter(Q(sender=request.user) | Q(receiver=request.user))
        abra_messages_qs_main = abra_messages_qs.filter(msg_read=False)
        abra_serializers = MessageSerializer(abra_messages_qs_main, many=True)
        return Response(abra_serializers.data, status=status.HTTP_200_OK)
