from lib.endpoints.methods import POST, PUT, GET, DELETE, AbstractMethod
from lib.endpoints.parameters import Str_Parameter, AbstractParameter


class Endpoint:
    def __init__(self, root, address, methods, parameters, auth_key) -> None:
        self.root = root
        self.address = address
        self.auth_key = auth_key
        self.methods: list[AbstractMethod] = methods
        self.parameters: list[AbstractParameter] = parameters

    def fuzz(self):
        for method in self.methods:
            method.fuzz(self.parameters)

    def test(self):
        self.send_request()

    def __repr__(self):
        return f"\n{self.address}:\n\t \
            Methods:{self.methods}\n\t \
            Parameters:{self.parameters}\n"

    def send_request(self):
        param_values = []
        for param in self.parameters:
            param_values.append(self.root + self.address.replace(
                param.original_value(),
                param.new_value()
            ))
        for m in self.methods:
            m.send_request(
                self.root+self.address,
                self.auth_key
            )

    @classmethod
    def new_endpoint(self, root, address, methods, auth_key):
        new_methods = []
        detected_parameters = []
        for m in methods:
            match m:
                case "GET":
                    new_methods.append(GET())
                case "POST":
                    new_methods.append(POST())
                case "PUT":
                    new_methods.append(PUT())
                case "DELETE":
                    new_methods.append(DELETE())
        for item in address.split("/"):
            if ":" in item:
                detected_parameters.append(Str_Parameter(item))

        return Endpoint(
            root,
            address,
            new_methods,
            detected_parameters,
            auth_key
        )
