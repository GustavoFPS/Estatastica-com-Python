import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd


def N(x, x0, s0):
    """_summary_

    Args:
        x (_type_): _description_
        x0 (_type_): _description_
        s0 (_type_): _description_
    """
    normal = (1/(np.sqrt(2*np.pi())*s0))*np.exp(- ((x - x0)**2)/(2*(s0**2)))
    return normal, x0, s0 

def simula(x0, s0, t):
    """_summary_

    Args:
        N (_type_): _description_
    """
    dados = []
    for i in range(0, t, 1):
        dados.append(np.random.normal(x0, s0))
        
    return dados

n , x0, s0 = 4, 0, 1 
sucesso = 0
i = 0
historias = 20
while i < historias:
    dados = simula(x0, s0, n)
    #print(len(dados))
    media = np.mean(dados)
    std = np.std(dados, ddof = 1)

    stdm = std/np.sqrt(n)

    if x0 >= media - stdm and x0 <= media + stdm: 
        sucesso += 1
    i += 1
alfa = 100* sucesso / historias 

print(alfa)

if alfa < 68.3:
    print("deu certo!")