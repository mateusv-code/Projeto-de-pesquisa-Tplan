import matplotlib.pyplot as plt
from qt_core import *
import numpy as np

class graficos(QMainWindow):
    def __init__(self, dx, colunas, cotas_plataforma_mista, mat_cotas, cota_adotada):
        super().__init__() # Boa prática inicializar a classe pai
        
        # Converte a lista de listas para array NumPy para permitir indexação [i, :]
        cotas_plataforma_mista = np.array(cotas_plataforma_mista)
        distancias = np.arange(0, colunas * dx, dx)
        
        # Número de seções é igual ao número de linhas da matriz
        num_secoes = mat_cotas.shape[0]

        for i in range(num_secoes):
            # --- 1. PREPARAÇÃO DOS DADOS DA SEÇÃO ATUAL ---
            terreno_natural = mat_cotas[i, :]
            cota_projeto = cotas_plataforma_mista[i, :]
            cota_plat = np.full(colunas, cota_adotada) # Cria array preenchida com a cota

            # --- 2. CONFIGURAÇÃO DO GRÁFICO ---
            plt.figure(figsize=(10, 6))

            # Plotagem das linhas principais
            plt.plot(distancias, terreno_natural, color='#00FF00', label='TERRENO NATURAL', linewidth=1)
            plt.plot(distancias, cota_projeto, color='#FF0000', label='PROJETO', linewidth=1)
            plt.plot(distancias, cota_plat, color='black', linestyle=':', label='PLATAFORMA', alpha=0.7)

            # Adicionando as linhas tracejadas verticais
            for x, y_terreno, y_projeto in zip(distancias, terreno_natural, cota_projeto):
                plt.vlines(x, ymin=min(y_terreno, y_projeto), ymax=max(y_terreno, y_projeto), 
                           colors='black', linestyles='--')
            
            # Texto da cota adotada no último ponto
            plt.text(distancias[-1], cota_adotada, f'{cota_adotada}', verticalalignment='center')

            # --- 3. ESTILIZAÇÃO TÉCNICA ---
            plt.title(f"Seção Longitudinal {i + 1}", fontsize=14, fontweight='bold')
            plt.xlabel("TERRENO", fontsize=12)
            plt.ylabel("COTA", fontsize=12)

            plt.grid(True, which='both', linestyle='-', alpha=0.2)
            plt.legend(loc='upper right', frameon=True, edgecolor='black')

            # Ajuste dinâmico dos limites Y para cada seção
            margem = 1.0
            plt.xlim(min(distancias) - 5, max(distancias) + 5)
            plt.ylim(min(np.min(terreno_natural), cota_adotada) - margem, 
                     max(np.max(terreno_natural), cota_adotada) + margem)

            plt.tight_layout()
            
        # Exibe todas as janelas de uma vez ao final do loop
        plt.show()