from rest_framework import serializers

from ..models.Products import Products

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Products
        fields = '__all__'