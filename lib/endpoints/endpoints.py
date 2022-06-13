from .endpoint import Endpoint


class Endpoints:
    def __init__(self, root) -> None:
        self.root = root
        self.endpoints = []

    def add_endpoint(self, endpoint: Endpoint):
        self.endpoints.append(endpoint)

    def test_endpoints(self):
        for endpoint in self.endpoints:
            try:
                endpoint.test()
            except Exception as e:
                print(f"{endpoint.address} failed with error: {e}")

    def fuzz_endpoints(self):
        for endpoint in self.endpoints:
            endpoint.fuzz()

    @classmethod
    def new_endpoints(self, root, endpoint_addresses, auth_key):
        endpoints = Endpoints(root)
        for e in endpoint_addresses:
            for k in e.keys():
                endpoints.add_endpoint(
                    Endpoint.new_endpoint(root, k, e[k]["methods"], auth_key)
                )
        return endpoints
