from examples.repositories.example_repository import ExampleRepository
from examples.dto.example_dto import ExampleDTO


class ExampleService:

    _repository: ExampleRepository

    def __init__(self, *args, **kwargs) -> None:
        self._repository = ExampleRepository
        pass

    def get_repository(self) -> any:
        return self._repository()

    def get(self, query_params: ExampleDTO) -> any:
        return self._repository().get(query_params)

    def create(self, data: dict) -> any:
        return self._repository().create(data)

    def get_by_id(self, id: int) -> any:
        return self._repository().get_by_id(id)

    def update(self, id: int, data: dict) -> any:
        return self._repository().update(id, data)

    def delete(self, id: int) -> any:
        return self._repository().delete(id)
