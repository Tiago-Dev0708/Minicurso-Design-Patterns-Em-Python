import random

class DbConnector:
    def __init__(self):
        self._id = random.randint(1, 100)
        print(self._id)

    def conectar(self):
        print("Conectado ao banco de dados")

db_connector = DbConnector()