from lib.endpoints.methods.abstractmethod import AbstractMethod


class GET(AbstractMethod):
    def __init__(self) -> None:
        super().__init__("GET")

    def test(self, parameters):
        print(
            f"sending GET request with these parameters: {parameters}"
            )

    def fuzz(self, parameters):
        print(
            f"fuzzing GET request with these parameters: {parameters}"
            )
