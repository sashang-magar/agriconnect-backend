from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet 
from rest_framework.views import APIView
from accounts.serializers import UserRegistrationSerializer , UserLoginSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny ,IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
class RegisterView(APIView):
    permission_classes=[AllowAny]

    def post(self, request): 
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "User registered successfully"} , status=status.HTTP_201_CREATED)
            

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self , request):
        serializer = UserLoginSerializer(data=request.data)   
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'role': user.role,
                'phone': user.phone,
                'district': user.district,
            },
            'message': 'Login successful'
        }, status=status.HTTP_200_OK) 
