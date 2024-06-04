from rest_framework.views import APIView
from bedjango.handler.response import Response


class BaseAPIView(APIView):
    def __init__(self):
        self.response = Response()
        
