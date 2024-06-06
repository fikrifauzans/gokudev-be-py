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
        self._service = ExampleService()
        self._dto = ExampleDTO

    def get_service(self) -> ExampleService:
        return self._service

    def get_dto(self, request) -> ExampleDTO:
        return self._dto(request)

    def get(self, request: any, format=None) -> Response:
        query_params: ExampleDTO = self.get_dto(request)
        data: dict = self.get_service().get(query_params)
        return (
            self.response()
            .set_message(DEFAULT_MESSAGE_HTTP_200)
            .set_code(status.HTTP_200_OK)
            .set_meta(data.meta)
            .set_data(data.data)
            .get_response()
        )

    def post(self, request, format=None) -> Response:
        dto: ExampleDTO = self.get_dto(request)
        created_data = self.get_service().create(dto._body_set)
        return (
            self.response()
            .set_message(DEFAULT_MESSAGE_HTTP_201)
            .set_code(status.HTTP_201_CREATED)
            .set_data(created_data)
            .get_response()
        )


class ExampleDetail(BaseAPIView):

    _service: ExampleService

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._service = ExampleService()

    def get_object(self, pk):
        return self._service.get_by_id(pk)

    def get(self, request, pk, format=None):
        obj = self.get_object(pk)
        if obj:
            return Response(obj, status=status.HTTP_200_OK)
        return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        if obj:
            updated_data = self._service.update(pk, request.data)
            return Response(updated_data, status=status.HTTP_200_OK)
        return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        if obj:
            self._service.delete(pk)
            return Response(
                {"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT
            )
        return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)
