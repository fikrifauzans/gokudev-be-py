from examples.repositories.example_repository import ExampleRepository


class ExampleService:

    _repository: ExampleRepository

    def __init__(self, *args, **kwargs) -> (None):
        self._repository = ExampleRepository
        pass

    def get_repository(self) -> (ExampleRepository):
        return self._repository()


    def get(self, request) -> (ExampleRepository):
        return self._repository().get(request)
