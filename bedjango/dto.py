class DTO:

    def __init__(self) -> None:
        pass

    def replace_like_to_icontains(self, query_set: dict[str, str]) -> dict[str, str]:
        q = {}
        for key, value in query_set.items():
            if "like" in key:
                q[f"{key.replace('like', 'icontains')}"] = query_set[key]
        return q

    def set_is_null(self, query):
        query["deleted_at__isnull"] = True
        return query
