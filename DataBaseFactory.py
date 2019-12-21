from AbstractFactory import AbstractFactory
from PSQLSaver import PSQLSaver
from RedisSaver import RedisSaver


class DataBaseFactory(AbstractFactory):

    def CreateFactory(self, type):
        if type == 'postgreSQL':
            return PSQLSaver()
        elif type == 'redis':
            return RedisSaver()