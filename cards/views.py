from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Cards
from .serializer import CardSerializer

# Create your views here.

class CardList(APIView):
    def get(self, request, format=None):
        all_cards = Cards.objects.all()
        serializers = CardSerializer(all_cards, many= True)
        return Response(serializers.data)