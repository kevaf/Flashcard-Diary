from rest_framework import serializers
from .models import Cards

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = ('title', 'notes', 'courses', 'pub_date')
        