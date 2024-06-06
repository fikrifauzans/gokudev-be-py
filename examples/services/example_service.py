from examples.repositories.example_repository import ExampleRepository
from examples.dto.example_dto import ExampleDTO


class ExampleService:

    _repository: ExampleRepository

    def __init__(self, *args, **kwargs) -> None:
        self._repository = ExampleRepository
        pass

    def get_repository(self) -> ExampleRepository:
        return self._repository()

    def get(self, query_params: ExampleDTO) -> ExampleRepository:
        return self._repository().get(query_params)
