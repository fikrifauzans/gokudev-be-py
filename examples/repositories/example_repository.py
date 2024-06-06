from examples.dto.example_dto import ExampleDTO
from examples.models.example_model import ExampleModel as Model
from bedjango.repository import GeneralRepository
from examples.serializers.example_serializer import ExampleSerializer as Serializer


class ExampleRepository(GeneralRepository):
    serializer: Serializer
    model: Model

    def __init__(self, *args, **kwargs) -> None:
        self.model = Model
        self.serializer = Serializer
        super().__init__(*args, **kwargs)

    def get(self, query_params: ExampleDTO) -> any:

        filtered_queryset = self.model.objects.filter(**query_params._query_set)

        return self.paginate_if_has_request_page_and_page_size(
            query_params, filtered_queryset, self.serializer
        )
