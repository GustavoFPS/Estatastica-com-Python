import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
import pandas as pd


def boxplot1(data_boxplot, x_label, y_label, tick = None):
    """Create a boxplot with scatter points.
    
    Args:
        data_boxplot (list): The data for the boxplot.
        x_label (str): The label for the x-axis.
        y_label (str): The label for the y-axis.
        tick (list or None): The tick labels for the x-axis. If None, x-axis tick labels are removed.
        
    Returns:
        None
        
    Examples:
        boxplot1([data1, data2], 'X Label', 'Y Label', ['A', 'B', 'C'])
    """

    # Criar a figura e os eixos
    fig, ax = plt.subplots()

    # Plotar o boxplot
    #box = ax.boxplot(data_boxplot, patch_artist=True, showfliers=False, boxprops=dict(facecolor='cadetblue'))

    # Ajustar a ordem das camadas de desenho 
    ax.set_zorder(2)  # Definir a ordem de desenho dos eixos para a frente
    
    if type(data_boxplot) != list:
        x_scatter = np.full_like(data_boxplot, 1) + np.random.uniform(-0.055, 0.055, len(data_boxplot))
        ax.scatter(x_scatter, data_boxplot, color='red', alpha=1, zorder=3, s= 15)
    else:
        for i, box_data in enumerate(data_boxplot, start=1):
            x_scatter = np.full_like(box_data, i) + np.full_like(box_data, np.random.uniform(-0.1, 0.1))
            ax.scatter(x_scatter, box_data, color='red', alpha=1, zorder=3, s= 15)  # Definir a ordem de desenho dos pontos de dispersão para a frente

    # Configurações adicionais
    ax.set_title('Boxplot com distribuição de pontos')
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    
    # Remover os rótulos do eixo x
    if tick is None:
        ax.set_xticklabels([])
        ax.tick_params(axis='x', which='both', bottom=False)
    else:
        ax.set_xticklabels(tick)
    # Mostrar o gráfico
    plt.show()

def boxplot2(data_boxplot, x_label, y_label):
    
    fig, ax = plt.subplots()
    box = ax.boxplot(data_boxplot, patch_artist=True, showfliers=True, showmeans=True, 
                boxprops=dict(facecolor='cadetblue'), meanprops=dict(marker='D', markerfacecolor='orange', markeredgecolor='black', markersize=8),
                flierprops=dict(marker='o', markerfacecolor='black', markersize=4, alpha=0.5))
    
    ax.set_xticklabels([])
    ax.tick_params(axis='x', which='both', bottom=False)
    ax.set_title('Boxplot com representação da média')
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.show()

def boxplot3(data_boxplot, x_label, y_label):    

    fig, ax = plt.subplots()

    # Plotar o boxplot
    box = ax.boxplot(data_boxplot, patch_artist=True, showfliers=False, boxprops=dict(facecolor='cadetblue'))

    # Ajustar a ordem das camadas de desenho
    ax.set_zorder(2)  # Definir a ordem de desenho dos eixos para a frente

    if type(data_boxplot[0]) != list:
        x_scatter = np.full_like(data_boxplot, 1) + np.random.uniform(0.1, 0.15, len(data_boxplot))
        ax.scatter(x_scatter, data_boxplot, color='red', alpha=1, zorder=3, s= 15)
    else:
        for i, box_data in enumerate(data_boxplot, start=1):
            x_scatter = np.full_like(box_data, i) + np.random.uniform(0.2, 0.3, len(box_data))
            ax.scatter(x_scatter, box_data, color='red', alpha=1, zorder=3, s= 15)  # Definir a ordem de desenho dos pontos de dispersão para a frente

    # Configurações adicionais
    ax.set_xticklabels([])
    ax.tick_params(axis='x', which='both', bottom=False)
    ax.set_title('Boxplot com distribuição externa de pontos')
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    # Mostrar o gráfico
    plt.show()

# Função para calcular os limites do intervalo de confiança
def calculate_confidence_interval(data, k=1):
    mean = np.mean(data)
    std_dev = np.std(data)
    lower_bound = mean - k * std_dev
    upper_bound = mean + k * std_dev
    return lower_bound, upper_bound


def boxplot4(data_boxplot, x_label, y_label, k = 1, ax = None):
    
    if ax is None:
        fig, ax = plt.subplots()
    else:
        fig = ax.figure

    # Ajustar a ordem das camadas de desenho
    ax.set_zorder(1)  # Definir a ordem de desenho dos eixos para a frente

    # Plotar o boxplot sem mostrar os outliers
    box = ax.boxplot(data_boxplot, patch_artist=True, showfliers=True, showmeans= True, boxprops=dict(facecolor='cadetblue'), flierprops=dict(marker='o', markerfacecolor='black', markersize=4, alpha=0.5), meanprops=dict(marker='D', markerfacecolor='orange', markeredgecolor='black', markersize=4))
        
        # Calcular os limites do intervalo de confiança para o boxplot atual
    lower_bound, upper_bound = calculate_confidence_interval(data_boxplot, k=k)
    # Adicionar retângulo para o intervalo de confiança
    rect = Rectangle((1 - 0.015, lower_bound), 0.03, upper_bound - lower_bound, linewidth=1, edgecolor='gray', facecolor='gray', zorder=2, alpha = 0.75)
    ax.add_patch(rect)

    # Adicionar sinal de mais no centro do retângulo
    #ax.text(1, (lower_bound + upper_bound) / 2, '+', color='black', fontsize=10, ha='center', va='center')

    # Configurações adicionais
    mean_symbol = r'$\bar{x} \ $'  # Símbolo de média (x̄)
    std_dev_symbol = r'$+ \ k \ \sigma_x  $'  # Símbolo do desvio padrão (σ) multiplicado por k
    title = f'Boxplot com e intervalo de confiança\n({mean_symbol} {std_dev_symbol})'
    ax.set_xticklabels([])
    ax.tick_params(axis='x', which='both', bottom=False)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    return fig, ax

'''# Carregar o arquivo Excel
df = pd.read_excel('Cópia de EnqueteBolinhas (editado).xlsx')

# Selecionar uma coluna específica do DataFrame e armazená-la em data_boxplot
boxplot1(data_boxplot, None,'Altura (cm)', ['Alunos'])'''
# Ler o arquivo Excel
df = pd.read_excel('Cópia de EnqueteBolinhas (editado).xlsx')

'''
# Nome da coluna que contém a informação sobre o uso de óculos
nome_da_coluna_oculos = 'Oculo'

nome_da_coluna = 'Bolinhas'

# Lista de alturas das pessoas que usam óculos
data_usa_oculos = df.loc[df[nome_da_coluna_oculos] >= "SIM" , nome_da_coluna].tolist()

# Lista de alturas das pessoas que não usam óculos
data_nao_usa_oculos = df.loc[df[nome_da_coluna_oculos] == "NÃO",nome_da_coluna].tolist()


data_pre = df[nome_da_coluna].tolist()

# Exibir os dados separados
print("Alturas das pessoas que usam óculos:", data_usa_oculos)
print("Alturas das pessoas que não usam óculos:", data_nao_usa_oculos)

data_boxplot = [data_pre, data_usa_oculos, data_nao_usa_oculos]
boxplot1(data_boxplot, None,'Nº de bolinhas', ['Total', 'Usam Óculos', "Não usam Óculos"])'''

'''
nome_da_coluna = 'Bolinhas'
data_boxplot = df[nome_da_coluna].tolist()


boxplot2(data_boxplot, None, 'Nº de bolinhas')'''
'''
nome_da_coluna = 'Bolinhas'
data_boxplot = df[nome_da_coluna].tolist()


boxplot3(data_boxplot, None, 'Nº de bolinhas')'''

nome_da_coluna = 'Altura'
data_boxplot = [df[df['Altura'] < 160], df[df['Altura'] >= 160]]
values_of_k = [0.5, 1, 2]

# Criar subplots para cada valor de k
#fig, axs = plt.subplots(1, len(values_of_k), figsize=(15, 5))
boxplot1(data_boxplot, None, 'Nº de bolinhas')
# Plotar cada boxplot com intervalo de confiança correspondente
'''for k, ax in zip(values_of_k, axs):
    
    ax.set_xlabel(f'k = {k}')
'''
# Ajustar layout
plt.tight_layout()

plt.show()


