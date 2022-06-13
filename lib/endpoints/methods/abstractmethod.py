from abc import ABC, abstractmethod
from urllib.request import urlopen, Request
from ssl import create_default_context, CERT_NONE

ctx = create_default_context()
ctx.check_hostname = False
ctx.verify_mode = CERT_NONE


class AbstractMethod(ABC):

    def __init__(self, method) -> None:
        self.method = method

    @classmethod
    @abstractmethod
    def test(self, parameters):
        pass

    @classmethod
    @abstractmethod
    def fuzz(self, parameters):
        pass

    def build_request(self, address, auth_key):
        header = {"Authorization": auth_key}
        return Request(address, headers=header, method=self.method)

    def send_request(self, address, auth_key):
        urlopen(self.build_request(address, auth_key), context=ctx)
