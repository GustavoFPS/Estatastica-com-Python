import numpy as np
import matplotlib.pyplot as plt
import sys

pos=[0.41, 0.68,1.41, 2.41, 3.79, 5.44, 7.47]
posicao = []
for element in pos:
  posicao.append(element*100)

tempo = [0.014, 0.1979,0.3854,0.5729,0.7604,0.9479,1.1354]

fit = np.polyfit(tempo, posicao, 2)
f = np.poly1d(fit)

label = str(" f(t) = {2:0.2f} t² + {1:0.2f} t + {0:0.2f}".format(f[0], f[1], f[2]))

plt.scatter(tempo, posicao)

plt.plot(tempo, f(tempo), c = 'r')
plt.title("Posição em função do tempo")
plt.xlabel('tempo (s)')
plt.ylabel('posição (cm)')
plt.text(0.5, 0.8, label)
plt.show()