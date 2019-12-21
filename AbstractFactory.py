from abc import ABC, abstractmethod

class AbstractFactory(ABC):

    @abstractmethod
    def CreateFactory(self, type):
        pass