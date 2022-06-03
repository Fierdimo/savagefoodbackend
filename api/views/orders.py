from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.authtoken.models import Token

from ..models import Orders
from ..serializers import OrderSerializer

from ..models.user import User
from ..serializers.UserSerializer import UserSerializer


class OrderView(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def user_data(self, request):
        # === Groups ===
        # Customer = 0
        # Admin = 1
        # Checker = 2
        # Delivery = 3
        user_id = Token.objects.get(key=request.auth).user_id
        user_query = User.objects.get(id=user_id)
        user_data = UserSerializer(user_query).data
        return user_data

    def list(self, request):
        if self.user_data(request)["group"] == 1 or self.user_data(request)["group"] == 2:
            return super().list(self, request)
        if self.user_data(request)["group"] == 3:
           #return Response (self.user_data(request)["id"])
            query = Orders.objects.filter(delivery_id=self.user_data(request)["id"])
            serializer = OrderSerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "Usuario no cuenta con dicho privilegio"}, status=status.HTTP_401_UNAUTHORIZED)
