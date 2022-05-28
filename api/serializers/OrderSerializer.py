from rest_framework import serializers

from ..models.Orders import Orders

class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Orders
        fields = '__all__'