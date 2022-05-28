from rest_framework import viewsets

from ..models import Products
from ..serializers import ProductSerializer

class ProductView(viewsets.ModelViewSet):    
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
        