from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from bedjango.handler.response import Response as CustomResponse
from rest_framework.exceptions import AuthenticationFailed, NotFound
import socket
import os


@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email")
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")

    if None in [username, password, email, first_name, last_name]:
        return Response(
            {"error": "Please provide all required fields"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    if User.objects.filter(username=username).exists():
        return Response(
            {"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST
        )

    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
    return Response(
        {
            "success": "User created successfully",
            "status": status.HTTP_201_CREATED,
            "user": user.username
        },
        status=status.HTTP_201_CREATED
    )


@api_view(["POST"])
def logout_view(request):
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(
            {"success": "Logged out successfully"}, status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    
class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            tokens = response.data
            custom_response = CustomResponse()
            custom_response.set_message("Data Found")
            custom_response.set_code(status.HTTP_200_OK)
            custom_response.set_data({
                "refresh": tokens.get("refresh"),
                "access": tokens.get("access")
            })
        except AuthenticationFailed:
            custom_response = CustomResponse()
            custom_response.set_message("Authentication failed: Wrong username or password")
            custom_response.set_code(status.HTTP_401_UNAUTHORIZED)
        except NotFound:
            custom_response = CustomResponse()
            custom_response.set_message("User not found")
            custom_response.set_code(status.HTTP_404_NOT_FOUND)
        except Exception as e:
            custom_response = CustomResponse()
            custom_response.set_message(str(e))
            custom_response.set_code(status.HTTP_400_BAD_REQUEST)

        custom_response.set_meta({})
        return custom_response.get_response()


