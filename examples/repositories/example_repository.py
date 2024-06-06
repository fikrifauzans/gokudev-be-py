from examples.models.example_model import ExampleModel as Model
from examples.serializers.example_serializer import ExampleSerializer as Serializer


class ExampleRepository:
    def __init__(self) -> (None):
        pass

    def get(self, request) -> (any):
        
        model = Model.objects.all()
        serializer = Serializer(model, many=True)
    
        return {"data": serializer.data}
