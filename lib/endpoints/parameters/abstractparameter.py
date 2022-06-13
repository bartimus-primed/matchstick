from abc import ABC, abstractmethod


class AbstractParameter(ABC):

    def __init__(self, parameter_name) -> None:
        self.optional = "?" in parameter_name
        self.parameter = parameter_name.strip(":").strip("?")

    @classmethod
    @abstractmethod
    def fuzzed(self):
        pass

    @classmethod
    @abstractmethod
    def new_value(self):
        pass

    def original_value(self):
        v = ":" + self.parameter
        if self.optional:
            return v + "?"
        return v

    def __repr__(self):
        return f"\nParam Name:{self.parameter} Optional:{self.optional}"
