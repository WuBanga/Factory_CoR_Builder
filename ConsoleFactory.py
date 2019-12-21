from AbstractFactory import AbstractFactory
from ConsoleSaver import ConsoleSaver

class ConsoleFactory(AbstractFactory):

    def CreateFactory(self, type):
        if type == 'Console':
            return ConsoleSaver()