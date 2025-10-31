import random

class DbConnector:
    _instancia = None

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super(DbConnector, cls).__new__(cls)
        return cls._instancia
    
    def __init__(self):
        if not hasattr(self, '_inicializado'):
            self._id = random.randint(1, 100)
            print("ID da conexão: {}".format(self._id))
            self._inicializado = True

    def conectar(self):
        print("Conectado ao Banco de Dados")