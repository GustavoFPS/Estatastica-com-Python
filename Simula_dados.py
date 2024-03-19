import numpy as np 
import random 
import matplotlib.pyplot as plt

gen = np.random.default_rng()

def demo_random():

    array = gen.integers(1, 6, size = 5, endpoint= True)

    print(array)

nlances = 1000
ndados = 5

dados = gen.integers(1, 6, size = (nlances, 5), endpoint= True)
soma = dados.sum(axis = 1)

mean = soma.mean()

plt.hist(soma)
lab = "media {0}".format(mean)
lab = str(lab)
print(lab)
plt.axvline(mean, c = 'r', linestyle = "--", label = lab)
plt.show()
