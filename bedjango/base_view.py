from rest_framework.views import APIView
from bedjango.handler.response import Response


class BaseAPIView(APIView):

    _response = Response

    def __init__(self):
        super().__init__()
        self._response = Response

    def get_response(self) -> Response():
        return self._response()
