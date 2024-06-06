from bedjango.view import BaseAPIView
from rest_framework.response import Response
from rest_framework import status
from bedjango.handler.status_message import *
from examples.services.example_service import ExampleService
from examples.dto.example_dto import ExampleDTO


class ExampleList(BaseAPIView):

    _service: ExampleService
    _dto: ExampleDTO

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._service = ExampleService
        self._dto = ExampleDTO

    def get_service(self) -> ExampleService:
        return self._service()

    def get_dto(self, query_set) -> ExampleDTO:
        return self._dto(query_set)

    def get(self, request: any, format=None) -> Response:
        query_params: ExampleDTO = self.get_dto(request)
        data: dict = self.get_service().get(query_params)
        return (
            self.get_response()
            .set_message(DEFAULT_MESSAGE_HTTP_200)
            .set_code(status.HTTP_200_OK)
            .set_meta({})
            .set_data(data)
            .get_response()
        )

    def post(self, request, format=None) -> Response:

        return (
            self.get_response()
            .set_message(DEFAULT_MESSAGE_HTTP_201)
            .set_code(status.HTTP_201_CREATED)
            .set_meta({})
            .set_data({})
            .get_response()
        )


class ExampleDetail(BaseAPIView):

    def get_object(self, pk):
        # try:
        #     return Snippet.objects.get(pk=pk)
        # except Snippet.DoesNotExist:
        #     raise Http404
        return Response({})

    def get(self, request, pk, format=None):
        # snippet = self.get_object(pk)
        # serializer = SnippetSerializer(snippet)
        # return Response(serializer.data)
        return Response({})

    def put(self, request, pk, format=None):
        # snippet = self.get_object(pk)
        # serializer = SnippetSerializer(snippet, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({})

    def delete(self, request, pk, format=None):
        # snippet = self.get_object(pk)
        # snippet.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({})
