from FactoryProducer import FactoryProducer
import json


if __name__ == '__main__':
    types = {'Database', 'Console', 'Email'}

    factoryPSQL = FactoryProducer.GetFactory('Database')
    PSQL = factoryPSQL.CreateFactory('postgreSQL')

    factoryRedis = FactoryProducer.GetFactory('Database')
    redis = factoryRedis.CreateFactory('redis')

    factoryConsole = FactoryProducer.GetFactory('Console')
    console = factoryConsole.CreateFactory('Console')

    factoryEmail = FactoryProducer.GetFactory('Email')
    email = factoryEmail.CreateFactory('Email')

    with open('logs.txt', 'r') as f1:
        txtlogs = f1.readlines()

    with open('logs.json', 'r') as f2:
        jsonlogs = json.load(f2)

    PSQL.set_next(console).set_next(email)
    for i in txtlogs:
        PSQL.handle(i)

    print('\nFrom JSON\n')

    redis.set_next(console)
    for j in jsonlogs:
        redis.handle(j)