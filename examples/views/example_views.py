from rest_framework.views import APIView
from bedjango.base_view import BaseAPIView
from rest_framework.response import Response


class ExampleList(BaseAPIView):

    def get(self, request, format=None):
        # snippets = Snippet.objects.all()
        # serializer = SnippetSerializer(snippets, many=True)
        # return Response(serializer.data)
        return Response({})

    def post(self, request, format=None):
        #     serializer = SnippetSerializer(data=request.data)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response(serializer.data, status=status.HTTP_201_CREATED)
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({})


class ExampleDetail(APIView):

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
