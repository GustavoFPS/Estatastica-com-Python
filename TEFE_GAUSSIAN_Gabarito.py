import numpy as np
import matplotlib.pyplot as plt

x0 = 20
s0 = 3 
n = 400
historias = 20 

medidas = np.random.normal(x0, s0, size = (historias, n))

media = np.mean(medidas, axis = 1)
std = np.std(medidas, axis =1, ddof = 1)

sm = std/(np.sqrt(n))

limInferior = media - sm <= x0
limSuperior = media + sm >= x0

n_sucesso = np.where(limInferior&limSuperior)[0].shape[0]

alfa = 100*n_sucesso/historias
print("o alfa é ", alfa)

t = (media - x0)/sm

inf = int(np.round(historias*(1-0.683)/2, decimals= 0))
sup = int(np.round(historias*(1+0.683)/2, decimals= 0))

z = np.sort(t)

plt.hist(t, bins = 20, ec = 'k')
plt.axvline(z[inf], color= 'r',linestyle = '--')
plt.axvline(z[sup], color= 'r',linestyle = '--')
plt.show()