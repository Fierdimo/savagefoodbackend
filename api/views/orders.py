from rest_framework import viewsets

from ..models import Orders
from ..serializers import OrderSerializer

class OrderView(viewsets.ModelViewSet):    
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer