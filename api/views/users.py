from tokenize import group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

import environ

from ..models.user import User
from ..serializers.UserSerializer import UserSerializer


class UserView(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
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
        if self.user_data(request)["group"] == 1:
            return super().list(self, request)

        if self.user_data(request)["group"] == 2:
            user_query = User.objects.filter(group=3)
            delivers = UserSerializer(user_query, many=True).data
            delivers = map(lambda data:
                {"full_name": data["name"]+" " +
                    data["last_name"], "id": data["id"]},
                delivers)
            return Response(delivers)

        return Response({"detail": "Usuario no cuenta con dicho privilegio"}, status=status.HTTP_401_UNAUTHORIZED)

    def create(self, request):
        user_data = self.user_data(request)
        if user_data["group"] == 1:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response("Usuario no cuenta con dicho privilegio", status=status.HTTP_401_UNAUTHORIZED)

    def retrieve(self, request, pk=None):
        user_data = self.user_data(request)
        if not user_data["group"] == 1:
           return Response(user_data)
        return super().retrieve(self, request, pk=None)


class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, format=None):
        request.user.auth_token.delete()
        return Response({'loged-out'}, status=status.HTTP_200_OK)


class NewCustomer(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def list(self, request):
        return Response('Accion invalida')    
    def retrieve (self,request,pk=None):
        return Response('Accion invalida')
    def update (self,request,pk=None):
        return Response('Accion invalida')
    def partial_update (self,request,pk=None):
        return Response('Accion invalida')
    def destroy (self,request,pk=None):
        return Response('Accion invalida')
    
    def create(self, request):
        
        data=request.data
        data._mutable = True
        data["group"] = 0
        data['option'] = ''
        data._mutable = False
        print(data)

        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response('Ups...! Algo salió mal', status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    def put(self, request):
        # print(request.data['username'])
        query = User.objects.filter(username=request.data["username_0"])
        if query:
            return Response({"forbidden"})
        
        return Response({"pass"})
    
    
class NewAdmin(APIView):
    
    
    def post(self, request):
        env = environ.Env()
        environ.Env.read_env()
    
        data=request.data
        
        if data['Key'] == env('SECRET_KEY'):
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response ('Formato de datos invalido')
        else:
            return Response ('No son los androides que buscabas')
            
    
class CustomAuthToken(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'group': user.group,
            'username': user.username,
        })