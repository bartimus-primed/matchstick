from lib.endpoints.methods.abstractmethod import AbstractMethod


class DELETE(AbstractMethod):
    def __init__(self) -> None:
        super().__init__("DELETE")

    def test(self, parameters):
        print(
            f"sending DELETE request with these parameters: {parameters}"
            )

    def fuzz(self, parameters):
        print(
            f"fuzzing DELETE request with these parameters: {parameters}"
            )
