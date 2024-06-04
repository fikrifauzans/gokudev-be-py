from rest_framework.response import Response as Res


class Response:
    message: str
    code: int
    data: dict
    meta: dict
    tokens: dict

    def __init__(self, message: str = "", code: int = 0, data: dict = None, tokens: dict = None):
        self.message = message
        self.code = code
        self.data = data if data is not None else {}
        self.tokens = tokens if tokens is not None else {}

    def set_tokens(self, tokens: dict) -> "Response":
        self.tokens = tokens
        return self

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
    
    def get_tokens(self) -> dict:
        return self.tokens

    def get_message(self) -> str:
        return self.message

    def get_code(self) -> int:
        return self.code

    def get_data(self) -> dict:
        return self.data

    def get_meta(self) -> dict:
        return self.meta

    def get_response(self) -> Res:
        response_data = {
            "status": self.get_code(),
            "message": self.get_message(),
            "data": self.get_data(),
            "meta": self.get_meta(),
        }
        if self.tokens:
            response_data["data"].update(self.tokens)  # Menambahkan tokens ke data jika ada
        return Res(response_data, self.get_code())
