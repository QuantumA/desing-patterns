from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass

class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
    
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None

class CallCenterHandler(AbstractHandler):
    
    def handle(self, request: Any) -> str:
        if request in ['internet', 'mobile', 'theft', 'commercial', 'invoice']:
            return super().handle(request)
        
        return f'Sorry I can´t help you'


class InternetConnectionHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == 'internet':
            return f'Internet connection handler is working'
        
        return super().handle(request)
  
class MobileTheftHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == 'theft':
            return f'We are going to help you with'
        
        return super().handle(request)

class InvoiceProblemHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == 'invoice':
            return f'Which problem do you have?'
        
        return super().handle(request)

class CommercialHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == 'commercial':
            return f'You need commercial asistance'
        
        return super().handle(request)


def client_code(handler: Handler) -> None:
    """
    The client code is usually suited to work with a single handler. In most
    cases, it is not even aware that the handler is part of a chain.
    """

    for reason in ["internet", "invoice", "theft", "fake", "commercial"]:
        print(f"\nClient: need help with {reason}")
        result = handler.handle(reason)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  We cant help you with that issue {reason}.", end="")


if __name__ == "__main__":
    invoice = InvoiceProblemHandler()
    commercial = CommercialHandler()
    theft = MobileTheftHandler()
    internet = InternetConnectionHandler()
    callcenter = CallCenterHandler()

    callcenter.set_next(invoice).set_next(commercial).set_next(theft).set_next(internet)

    print("Chain: Monkey > Squirrel > Dog")
    client_code(callcenter)
    print("\n")