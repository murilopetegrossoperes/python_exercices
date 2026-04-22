#O objetivo deste exercício é processar uma matriz de tamanho fixo 4 X 4. Você deve analisar cada elemento inserido para identificar quantos deles atendem a critérios específicos de magnitude e sinal.
indice = 0
n_linhas = 4
n_colunas = 4
qtd_maior_10 = 0
qtd_menor_0 = 0

matriz = [[0 for c in range(n_colunas)] for l in range(n_linhas)]
itens_linha = input().split(",")

for linha in range(n_linhas):
    for coluna in range(n_colunas):
        matriz[linha][coluna] = int(itens_linha[indice])
        

        if int( matriz[linha][coluna]) > 10:
            qtd_maior_10 += 1
        if int( matriz[linha][coluna]) < 0:
            qtd_menor_0 += 1
        indice += 1
        
print(f"Maior que 10: {qtd_maior_10}")
print(f"Menor que 0: {qtd_menor_0}")

for i in range(n_linhas):
    for j in range(n_colunas):
             print(matriz[i][j], end=" ")
    print()
