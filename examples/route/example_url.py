from django.urls import path
from examples.views.example_views import ExampleDetail, ExampleList

urlpatterns = [
    path("example", ExampleList.as_view()),
    path("example/<int:pk>", ExampleDetail.as_view()),
]
