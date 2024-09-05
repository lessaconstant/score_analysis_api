from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import CustomUserSerializer

class UserListCreateView(APIView):
    def get(self, request):
        users = CustomUser.objects.all()  
        serializer = CustomUserSerializer(users, many=True)  
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return None

    def get(self, request, pk):
        user = self.get_object(pk)
        if user is not None:
            serializer = CustomUserSerializer(user)
            return Response(serializer.data)
        return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        user = self.get_object(pk)
        if user is not None:
            serializer = CustomUserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        user = self.get_object(pk)
        if user is not None:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)

class UserBankUpdateView(APIView):
    def put(self, request, pk):
        user = CustomUser.objects.get(pk=pk)
        banks_ids = request.data.get('banks', []) 
        user.banks.set(banks_ids)  
        user.save()
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
