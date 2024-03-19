import numpy as np 
import matplotlib.pyplot as plt

gen = np.random.default_rng()

nlances = 1000
ndados = 5
dados = gen.integers(1, 6, size = (nlances, 5), endpoint= True)

quadra = 0


for jogada in dados:
    score =  np.unique(jogada, return_counts=True)[1]
    print(score) 
    if 4 in np.unique(jogada, return_counts=True)[1]:
        quadra += 1

print(quadra)
  

print(quadra/1000)