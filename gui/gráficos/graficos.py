import matplotlib.pyplot as plt
from qt_core import *
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class graficos(QMainWindow):
    def __init__(self, dx, dy, colunas, cotas_plataforma_mista, mat_cotas, cota_adotada):
        super().__init__() # Boa prática inicializar a classe pai
        
        # Converte a lista de listas para array NumPy para permitir indexação [i, :]
        cotas_plataforma_mista = np.array(cotas_plataforma_mista)
        distancias = np.arange(0, colunas * dx, dx)
        
        # Número de seções é igual ao número de linhas da matriz
        num_secoes = mat_cotas.shape[0]

        # 1. Definição dos eixos com dx=dy=20
        x = np.arange(mat_cotas.shape[1]) * dx
        y = np.arange(mat_cotas.shape[0]) * dy
        X, Y = np.meshgrid(x, y)

        # 2. Ajuste da Matriz
        # O Matplotlib plota a primeira linha da matriz no y=0.
        # Se na sua tabela a primeira linha [1, 2, 3] é o "topo" (y=40),
        # precisamos inverter a matriz para o gráfico ficar correto.
        mat_corrigida = np.flipud(mat_cotas) 

        # 3. Gráfico
        plt.figure(figsize=(6, 5))

        niveis = np.arange(np.min(mat_cotas), np.max(mat_cotas) + 0.5, 0.5)

        # Usamos mat_corrigida para alinhar as cotas com as coordenadas Y
        curvas = plt.contour(X, Y, mat_corrigida, levels=niveis, cmap='jet', linestyles='dashed')

        plt.clabel(curvas, inline=True, fontsize=10, colors='black', fmt='%1.1f')

        # 4. Estilização final
        plt.title('CURVAS DE NÍVEL', fontweight='bold')
        plt.xlabel('TERRENO (X)')
        plt.ylabel('TERRENO (Y)')

        # Força os limites para 0 a 40
        plt.xlim(0, x.max())
        plt.ylim(0, y.max())

        plt.grid(True, which='both', linestyle='-', color='lightgrey', alpha=0.6)
        plt.gca().set_aspect('equal')


        for i in range(num_secoes):
            # --- 1. PREPARAÇÃO DOS DADOS DA SEÇÃO ATUAL ---
            terreno_natural = mat_cotas[i, :]
            cota_projeto = cotas_plataforma_mista[i, :]
            cota_plat = np.full(colunas, cota_adotada) # Cria array preenchida com a cota

            # --- 2. CONFIGURAÇÃO DO GRÁFICO ---
            plt.figure(figsize=(6, 5))

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

        # 1. Preparação dos Dados
        mat_cotas = np.array(mat_cotas)
        # x corresponde às colunas, y às linhas
        x = np.arange(mat_cotas.shape[1]) * dx
        y = np.arange(mat_cotas.shape[0]) * dy
        X, Y = np.meshgrid(x, y)

        # 2. Configuração da Figura 3D
        fig = plt.figure(figsize=(6, 5))
        ax = fig.add_subplot(111, projection='3d')

        # Desenho do Terreno (Superfície semi-transparente e Aramado tracejado)
        ax.plot_surface(X, Y, mat_cotas, color='lightblue', alpha=0.3, shade=True)
        ax.plot_wireframe(X, Y, mat_cotas, color='black', linestyle='--', linewidth=0.6)

        # 3. Inserção dos Valores das Cotas (Texto em Vermelho)
        # mat_cotas.shape[0] é o número de linhas (Y), shape[1] é o de colunas (X)
        for i in range(mat_cotas.shape[0]):
            for j in range(mat_cotas.shape[1]):
                ax.text(X[i, j], Y[i, j], mat_cotas[i, j] + 0.3, f'{mat_cotas[i, j]:.2f}', 
                        color='red', fontweight='bold', fontsize=10, ha='center', zorder=20)

        # 4. Construção das Faces Laterais (Efeito de Volume Sólido)
        base_z = 0
        faces = []
        
        # Laterais acompanhando as linhas (Y) - fixando X no início e no fim
        for i in range(mat_cotas.shape[0] - 1):
            # Lado Esquerdo (X=0)
            faces.append([(x[0], y[i], base_z), (x[0], y[i+1], base_z), 
                          (x[0], y[i+1], mat_cotas[i+1, 0]), (x[0], y[i], mat_cotas[i, 0])])
            # Lado Direito (X=Max)
            faces.append([(x[-1], y[i], base_z), (x[-1], y[i+1], base_z), 
                          (x[-1], y[i+1], mat_cotas[i+1, -1]), (x[-1], y[i], mat_cotas[i, -1])])

        # Laterais acompanhando as colunas (X) - fixando Y no início e no fim
        for j in range(mat_cotas.shape[1] - 1):
            # Frente (Y=0)
            faces.append([(x[j], y[0], base_z), (x[j+1], y[0], base_z), 
                          (x[j+1], y[0], mat_cotas[0, j+1]), (x[j], y[0], mat_cotas[0, j])])
            # Fundo (Y=Max)
            faces.append([(x[j], y[-1], base_z), (x[j+1], y[-1], base_z), 
                          (x[j+1], y[-1], mat_cotas[-1, j+1]), (x[j], y[-1], mat_cotas[-1, j])])

        # Adiciona a Base Inferior
        faces.append([(x[0], y[0], base_z), (x[-1], y[0], base_z), 
                      (x[-1], y[-1], base_z), (x[0], y[-1], base_z)])

        # Renderiza o volume cinza
        poly3d = Poly3DCollection(faces, facecolors='lightgray', linewidths=0.5, edgecolors='black', alpha=0.3)
        ax.add_collection3d(poly3d)

        # 5. Ajustes de Eixos e Títulos
        ax.set_title('TERRENO NATURAL - TPLAN', fontweight='bold', fontsize=12)
        ax.set_xlabel('COORDENADA X (m)')
        ax.set_ylabel('COORDENADA Y (m)')
        ax.set_zlabel('COTA (m)')

        # Ajusta os Ticks para mostrar os limites reais do terreno
        ax.set_xticks(x)
        ax.set_yticks(y)
        ax.set_zlim(0, np.max(mat_cotas) + 1)

        # Perspectiva padrão do MATLAB
        ax.view_init(elev=25, azim=-135)

        plt.tight_layout()

        # 1. Preparação dos Dados do Projeto
        # mat_projetada contém as cotas finais após a terraplenagem
        mat_projetada = np.array(cotas_plataforma_mista)

        # 2. Configuração da Figura 3D
        fig = plt.figure(figsize=(6, 5))
        ax = fig.add_subplot(111, projection='3d')

        # Desenho da Plataforma Projetada (Cor laranja/avermelhada para diferenciar do natural)
        ax.plot_surface(X, Y, mat_projetada, color='salmon', alpha=0.4, shade=True)
        ax.plot_wireframe(X, Y, mat_projetada, color='black', linestyle='--', linewidth=0.6)

        # 3. Inserção dos Valores das Cotas de Projeto
        for i in range(mat_projetada.shape[0]):
            for j in range(mat_projetada.shape[1]):
                ax.text(X[i, j], Y[i, j], mat_projetada[i, j] + 0.3, f'{mat_projetada[i, j]:.2f}', 
                        color='darkred', fontweight='bold', fontsize=10, ha='center', zorder=20)

        # 4. Construção das Faces Laterais (Volume do Projeto)
        base_z = 0
        faces = []
        
        # Laterais em X
        for i in range(mat_projetada.shape[0] - 1):
            faces.append([(x[0], y[i], base_z), (x[0], y[i+1], base_z), 
                          (x[0], y[i+1], mat_projetada[i+1, 0]), (x[0], y[i], mat_projetada[i, 0])])
            faces.append([(x[-1], y[i], base_z), (x[-1], y[i+1], base_z), 
                          (x[-1], y[i+1], mat_projetada[i+1, -1]), (x[-1], y[i], mat_projetada[i, -1])])

        # Laterais em Y
        for j in range(mat_projetada.shape[1] - 1):
            faces.append([(x[j], y[0], base_z), (x[j+1], y[0], base_z), 
                          (x[j+1], y[0], mat_projetada[0, j+1]), (x[j], y[0], mat_projetada[0, j])])
            faces.append([(x[j], y[-1], base_z), (x[j+1], y[-1], base_z), 
                          (x[j+1], y[-1], mat_projetada[-1, j+1]), (x[j], y[-1], mat_projetada[-1, j])])

        # Base
        faces.append([(x[0], y[0], base_z), (x[-1], y[0], base_z), 
                      (x[-1], y[-1], base_z), (x[0], y[-1], base_z)])

        poly3d = Poly3DCollection(faces, facecolors='rosybrown', linewidths=0.5, edgecolors='black', alpha=0.3)
        ax.add_collection3d(poly3d)

        # 5. Ajustes de Eixos e Títulos
        ax.set_title('TERRENO PROJETADO (PLATAFORMA)', fontweight='bold', fontsize=12)
        ax.set_xlabel('X (m)')
        ax.set_ylabel('Y (m)')
        ax.set_zlabel('COTA (m)')

        ax.set_xticks(x)
        ax.set_yticks(y)
        ax.set_zlim(0, np.max(mat_projetada) + 1)

        ax.view_init(elev=25, azim=-135)

        plt.tight_layout()

       

        # Exibe todas as janelas de uma vez ao final do loop
        plt.show()