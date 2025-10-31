import numpy as np
from facade import NumpyFacade as Np

lista = [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]
dados = Np.criar_array(lista)

print("Array 2D:\n", dados)

media_colunas = np.mean(dados, axis=0)
media_linhas = np.mean(dados, axis=1)
#media_colunas = np.mean(dados)
#media_linhas = np.mean(dados)
print(media_colunas)
print(media_linhas)