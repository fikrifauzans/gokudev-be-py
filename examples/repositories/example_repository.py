from examples.dto.example_dto import ExampleDTO
from examples.models.example_model import ExampleModel as Model
from bedjango.repository import GeneralRepository
from examples.serializers.example_serializer import ExampleSerializer as Serializer
from django.utils import timezone


class ExampleRepository(GeneralRepository):
    serializer: Serializer
    model: Model

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.model = Model
        self.serializer = Serializer
