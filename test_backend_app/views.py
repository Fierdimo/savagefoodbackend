from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from test_backend_app.models import Toy
from test_backend_app.serializers import ToySerializer

class Listar(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        
        toys = Toy.objects.all()
        toys_serializer = ToySerializer(toys, many=True)
        return Response(toys_serializer.data, status=status.HTTP_302_FOUND)

    def post(self, request):
        serializer = ToySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content['user'])


class Detail(APIView):

    def number_toy(self, pk_):
        try :
            self.toy = Toy.objects.get(pk=pk_)
            return True
        except Toy.DoesNotExist:
            return False

    def get(self, request):
        if self.number_toy(request.data.get('pk')):
            return Response(ToySerializer(self.toy).data, status=status.HTTP_302_FOUND)
        else:
            return Response({'Found':False},status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request):
        if self.number_toy(request.data.get('pk')):
            serializer = ToySerializer(self.toy, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'Found':False},status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        if self.number_toy(request.data.get('pk')):
            self.toy.delete()            
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'Found':False},status=status.HTTP_404_NOT_FOUND)