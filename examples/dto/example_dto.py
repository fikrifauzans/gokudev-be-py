from bedjango.dto import DTO


class ExampleDTO(DTO):
    _query_set: dict[str, str]
    _raw_request: any

    def __init__(self, request):
        super().__init__()
        
        # Replace FE like as icontains
        query: dict = self.replace_like_to_icontains(request.query_params)

        # Add Soft Delete Query
        self._query_set = self.set_is_null(query)
        
        # Add Raw Request 
        self._raw_request = request
      
        
