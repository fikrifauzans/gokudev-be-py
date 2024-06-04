from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
import socket


@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):

    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email")

    if username is None or password is None or email is None:
        return Response(
            {"error": "Please provide all required fields"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if User.objects.filter(username=username).exists():
        return Response(
            {"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST
        )

    user = User.objects.create_user(username=username, password=password, email=email)
    return Response(
        {"success": "User created successfully"}, status=status.HTTP_201_CREATED
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


def login_view(request):
    HOST = "localhost"  # The server's hostname or IP address
    PORT = 8000  # The port used by the server
    msg = {"username": request.data.username, "password": request.data.password}
    cl = len(msg)
    pr = f"POST api/auth HTTP/1.1\r\nHost:{HOST}:{PORT}\r\nContent-Type: application/json\r\nContent-Length: {cl}\r\n\r\n"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall((pr + msg).encode())
        response = s.recv(1024)  # Receive response from the server
    return response.decode()  # Assuming you want to return the response from the server
