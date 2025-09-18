
dx = 2
dy = 2

lista_coluna1 = [1,2]
lista_coluna2 = [2,3]
valores_matriz = [lista_coluna1,lista_coluna2]

        
linhas = len(valores_matriz)
colunas = len(valores_matriz[0])

volumes_de_corte_secoes = []
volumes_de_aterro_secoes = []

for i in range(linhas):
    volume_corte_secao = 0
    volume_aterro_secao = 0
        
    # Fator de multiplicação (bordas usam metade)
    if i == 0 or i == linhas - 1:
        fator = dy / 2
    else:
        fator = dy

    for j in range(colunas - 1):
        plat_h1 = 2
        plat_h2 = 2

        h1 = valores_matriz[i][j] - plat_h1
        h2 = valores_matriz[i][j+1] - plat_h2



        volume_corte = 0
        volume_aterro = 0

        if h1 >= 0 and h2 >= 0:
            # Todo em corte
            volume_corte = ((h1 + h2) / 2) * dx * fator

        elif h1 <= 0 and h2 <= 0:
            # Todo em aterro
            volume_aterro = ((abs(h1) + abs(h2)) / 2) * dx * fator

        else:
            # Houve interseção com a plataforma
            x_intersec = dx * (abs(h1) / (abs(h1) + abs(h2)))

            if h1 > 0:
            # ponto inicial em corte
                volume_corte = (h1 * x_intersec) / 2 * fator
                volume_aterro = (abs(h2) * (dx - x_intersec)) / 2 * fator
            else:
                # ponto inicial em aterro
                volume_aterro = (abs(h1) * x_intersec) / 2 * fator
                volume_corte = (h2 * (dx - x_intersec)) / 2 * fator

        volume_corte_secao += volume_corte
        volume_aterro_secao += volume_aterro
        print(volume_corte_secao)
        print(volume_aterro_secao)
    volumes_de_corte_secoes.append(volume_corte_secao)
    volumes_de_aterro_secoes.append(volume_aterro_secao)
        
print(f'{volumes_de_corte_secoes}')
print(f'{volumes_de_aterro_secoes}')