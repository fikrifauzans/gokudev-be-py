from bedjango.dto import DTO


class ExampleDTO(DTO):
    _query_set: dict[str, str]
    _raw_request: any
    _id: int | None
    _body_set: dict | None

    def __init__(self, request):
        super().__init__()
        self._raw_request = request
        self._id = None
        self._body_set = None

        if request.method == "GET":
            # Replace FE like as icontains
            query: dict = self.replace_like_to_icontains(request.query_params)

            # Add Soft Delete Query
            self._query_set = self.set_is_null(query)

        elif request.method in ["POST", "PUT", "DELETE"]:
            self._body_set = request.data

            if "id" in request.data:
                self._id = request.data["id"]
