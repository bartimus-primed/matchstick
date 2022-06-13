from lib.endpoints.methods.abstractmethod import AbstractMethod


class PUT(AbstractMethod):
    def __init__(self) -> None:
        super().__init__("PUT")

    def test(self, parameters):
        print(
            f"sending PUT request with these parameters: {parameters}"
            )

    def fuzz(self, parameters):
        print(
            f"fuzzing PUT request with these parameters: {parameters}"
            )
