#você deve processar uma matriz quadrada de dimensões n×n o desafio consiste em identificar todos os elementos que estão localizados abaixo da diagonal principal e, dentre esses, somar apenas os que forem números pares.
n =  int(input())
n_linhas = n
n_colunas = n
soma = 0
matriz = [[0 for c in range(n_colunas)] for l in range(n_linhas)]

for linha in range(n_linhas):
    itens_linha = input().split(" ")
    for coluna in range(n_colunas):
        matriz[linha][coluna] = int(itens_linha[coluna])

for i in range(n_linhas):
    for j in range(n_colunas):
        if i > j:
            if matriz[i][j] % 2 == 0:
                soma += matriz[i][j]
print(soma)