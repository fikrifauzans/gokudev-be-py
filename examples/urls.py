from django.urls import path, include

# from examples.models import
urlpatterns = [
    path("examples/", include("examples.route.example_url")),
    # ${GENERATOR_PARAM}
]
