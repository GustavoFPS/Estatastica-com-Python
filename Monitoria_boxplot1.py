import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
import pandas as pd

def boxplot(data_boxplot, x_label, y_label, tick = None, Title = 'Boxplot com distribuição de pontos'): 
    """Create a boxplot with scatter points.
    
    Args:
        data_boxplot (list): The data for the boxplot.
        x_label (str): The label for the x-axis.
        y_label (str): The label for the y-axis.
        tick (list or None): The tick labels for the x-axis. If None, x-axis tick labels are removed.
        
    Returns:
        None
        
    Examples:
        boxplot([data1, data2], 'X Label', 'Y Label', ['A', 'B', 'C'])
    """

    # Criar a figura e os eixos
    fig, ax = plt.subplots()

    # Plotar o boxplot
    box = ax.boxplot(data_boxplot, patch_artist=True, showfliers=True, showmeans= True,  boxprops=dict(facecolor='silver'),
                    meanprops=dict(marker='s', markerfacecolor='black', markeredgecolor='black', markersize=5),
                    flierprops=dict(marker='o', markerfacecolor='red',  markeredgecolor='red', markersize=4, alpha=1))
    
    # Adicionar um marcador manualmente para a legenda da média
    ax.plot([], [], marker='_', color='orange', label='Mediana', linestyle='None', markersize=5)
    ax.plot([], [], marker='s', color='black', label='Média', linestyle='None', markersize=5)
    ax.plot([], [], marker='o', color='red', label='Outliers', linestyle='None', markersize=5)

    # Ajustar a ordem das camadas de desenho 
    ax.set_zorder(2)  # Definir a ordem de desenho dos eixos para a frente
    
    if type(data_boxplot[0]) != list:
        x_scatter = np.full_like(data_boxplot, 1) + np.random.uniform(-0.055, 0.055, len(data_boxplot))
        ax.scatter(x_scatter, data_boxplot, color='red', alpha=1, zorder=3, s= 15)
    else:
        for i, box_data in enumerate(data_boxplot, start=1):
            x_scatter = np.full_like(box_data, i) + np.random.uniform(-0.05, 0.05, len(box_data))
            #ax.scatter(x_scatter, box_data, color='red', alpha=1, zorder=3, s= 10, label = 'Pontos' )  # Definir a ordem de desenho dos pontos de dispersão para a frente

    # Configurações adicionais
    ax.set_title(Title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    
    # Remover os rótulos do eixo x
    if tick is None:
        ax.set_xticklabels([])
        ax.tick_params(axis='x', which='both', bottom=False)
    else:
        ax.set_xticklabels(tick)
    # Mostrar o gráfico
    
    # plota legenda sinalizando os pontos, mediana e média
    ax.legend(loc='upper right')    
    return fig, ax

# Ler o arquivo Excel
df = pd.read_excel('Cópia de EnqueteBolinhas (editado).xlsx')


nome_da_coluna = 'Bolinhas'
data_boxplot = [df[nome_da_coluna][df['Altura'] < 160].tolist(), df[nome_da_coluna][df['Altura'] >= 160].tolist()]

values_of_k = [0.5, 1, 2]


boxplot(data_boxplot, 'Altura', 'Nº de bolinhas', tick= ['< 160', '>= 160'], Title = 'Boxplot com distribuição de pontos')

# Ajustar layout
plt.tight_layout()

plt.show()
