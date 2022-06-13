from lib.endpoints.methods.abstractmethod import AbstractMethod


class POST(AbstractMethod):
    def __init__(self) -> None:
        super().__init__("POST")

    def test(self, parameters):
        print(
            f"sending POST request with these parameters: {parameters}"
            )

    def fuzz(self, parameters):
        print(
            f"fuzzing POST request with these parameters: {parameters}"
            )
