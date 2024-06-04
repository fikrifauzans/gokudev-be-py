from bedjango.base_view import BaseAPIView
from rest_framework.response import Response
from rest_framework import status
from bedjango.handler.status_message import *

class ExampleList(BaseAPIView):

    def get(self, request, format=None):

        return (
            self.response.set_message(DEFAULT_MESSAGE_HTTP_200)
            .set_code(status.HTTP_200_OK)
            .set_meta({})
            .set_data({})
            .get_response()
        )

    def post(self, request, format=None):

        return (
            self.response.set_message(DEFAULT_MESSAGE_HTTP_201)
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
