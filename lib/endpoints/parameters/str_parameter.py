from lib.endpoints.parameters.abstractparameter import AbstractParameter


class Str_Parameter(AbstractParameter):
    def __init__(self, parameter_name) -> None:
        super().__init__(parameter_name)

    def fuzzed(self):
        return self.value()

    def new_value(self):
        return "randomvalue"
