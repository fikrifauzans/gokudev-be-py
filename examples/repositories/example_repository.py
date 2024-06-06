from examples.dto.example_dto import ExampleDTO
from examples.models.example_model import ExampleModel as Model
from bedjango.repository import GeneralRepository
from examples.serializers.example_serializer import ExampleSerializer
from django.core.paginator import Paginator


class ExampleRepository(GeneralRepository):

    def get(self, query_params: ExampleDTO) -> any:
     
        filtered_queryset = Model.objects.filter(**query_params._query_set)

        if query_params._raw_request.query_params.get("page_size") == None:
            return {
                "total": len(filtered_queryset.values()),
                "data": filtered_queryset.values(),
            }

        paginator = Paginator(
            filtered_queryset, query_params._raw_request.query_params.get("page_size", 10)
        )
        page = paginator.get_page(query_params._raw_request.query_params.get("page", 1))

        serializer = ExampleSerializer(page.object_list, many=True)
        return {
            "total": paginator.count,
            "total_pages": paginator.num_pages,  # Added total pages
            "next": page.next_page_number() if page.has_next() else None,
            "previous": page.previous_page_number() if page.has_previous() else None,
            "data": serializer.data,
        }
