from rest_framework.response import Response


class Response:
    message: str
    code: int
    data: dict
    meta: dict

    def __init__(self, message: str = "", code: int = 0, data: dict = None):
        self.message = message
        self.code = code
        self.data = data if data is not None else {}

    def set_message(self, message: str = "") -> "Response":
        self.message = message
        return self

    def set_code(self, code: int = 0) -> "Response":
        self.code = code
        return self

    def set_data(self, data: dict = {}) -> "Response":
        self.data = data
        return self

    def set_meta(self, meta: dict = {}) -> "Response":
        self.meta = meta
        return self

    def get_message(self) -> str:
        return self.message

    def get_status(self) -> int:
        return self.code

    def get_data(self) -> dict:
        return self.data

    def get_meta(self) -> dict:
        return self.meta

    def get_response(self) -> dict:
        return Response(
            {
                "status": self.get_status,
                "message": self.get_message,
                "data": self.get_data,
                "meta": self.get_meta,
            }
        )
