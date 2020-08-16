""" Pattern Structure
    Client
    AbstractFactory
    ConcreteFactories
    AbstractProduct
    ConcreteProduct
    https://www.youtube.com/watch?v=CVlpjFJN17U
    https://devexperto.com/patrones-de-diseno-software/
"""
from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    """AbstractProduct class for definition"""

    @abstractmethod
    def get_product_name(self):
        pass


class TeslaModelS(AbstractProduct):
    """ConcreteProduct"""

    def get_product_name(self):
        return "The Tesla model S"


class AbstractElonFactory(ABC):
    """AbstractFactory class for definition"""

    @abstractmethod
    def create_product_one():
        pass


class TeslaFactory(AbstractElonFactory):
    """ConcreteFactory"""

    def create_product_one(self):
        return TeslaModelS()


def client_code(factory: AbstractElonFactory) -> None:
    product = factory.create_product_one()
    name = product.get_product_name()
    print(name)


if __name__ == "__main__":
    client_code(TeslaFactory())
