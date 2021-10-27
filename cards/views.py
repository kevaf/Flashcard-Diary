from django.contrib.auth.decorators import login_required
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Cards
from .serializer import CardSerializer, UserSerializer, RegisterSerializer
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class CardList(LoginRequiredMixin,APIView):

    def get(self, request, format=None):
        all_cards = Cards.objects.all()
        serializers = CardSerializer(all_cards, many= True)
        return Response(serializers.data)
    
 
    def post(self, request, format=None):
        serializers = CardSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class CardDets(LoginRequiredMixin,APIView):
    
    def get_card(self, pk):
        try:
            return Cards.objects.get(pk=pk)
        except Cards.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        card = self.get_card(pk)
        serializers = CardSerializer(card)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        card = self.get_card(pk)
        serializers = CardSerializer(card, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        card = self.get_card(pk)
        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)