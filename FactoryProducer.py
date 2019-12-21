from DataBaseFactory import DataBaseFactory
from ConsoleFactory import ConsoleFactory
from EmailFactory import EmailFactory


class FactoryProducer:

    @staticmethod
    def GetFactory(type):
        if type == 'Database':
            return DataBaseFactory()
        elif type == 'Console':
            return ConsoleFactory()
        elif type == 'Email':
            return EmailFactory()