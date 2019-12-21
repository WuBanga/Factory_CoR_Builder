from AbstractFactory import AbstractFactory
from EmailSaver import EmailSaver


class EmailFactory(AbstractFactory):

    def CreateFactory(self, type):
        if type == 'Email':
            return EmailSaver()