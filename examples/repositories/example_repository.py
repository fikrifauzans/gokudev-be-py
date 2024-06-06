class ExampleRepository:
    def __init__(self) -> None:
        pass

    def get(self, request) -> any:
        return {"data": request.GET.get("req")}
