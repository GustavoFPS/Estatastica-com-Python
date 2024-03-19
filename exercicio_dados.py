import numpy as np 
import matplotlib.pyplot as plt

gen = np.random.default_rng()

nlances = 1000
ndados = 5
dados = gen.integers(1, 6, size = (nlances, 5), endpoint= True)
#dados = [[4, 4, 2 , 4, 4], [4, 4, 2 , 1, 4], [3, 2, 3 , 3, 3]]
quadra = 0


for jogada in dados:
     
    for element in jogada:
        count = 0 
        
        for dado in range(0, 5):
             
            if element == jogada[dado]:
                count += 1 
        if count == 4: 
            quadra += 1 
            break
     
print(quadra)   

print(quadra/1000)