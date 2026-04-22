#Neste desafio, você deve processar uma matriz de dimensões linhas X colunas. O sistema receberá os valores e seu programa deverá reorganizar os elementos dentro de cada linha de forma independente e crescente.

n_linhas = int(input())
n_colunas = int(input())

matriz = [[0 for c in range(n_colunas)] for l in range(n_linhas)]

for linha in range(n_linhas):
    itens_linha = input().split(" ")

    for coluna in range(n_colunas):
        matriz[linha][coluna] = int(itens_linha[coluna])

        for j in range(0, n_colunas - coluna - 1):
            
            if itens_linha[j] > itens_linha[j + 1]:
                itens_linha[j], itens_linha[j + 1] = itens_linha[j + 1], itens_linha[j]
                

        for coluna in range(n_colunas):
            matriz[linha][coluna] = int(itens_linha[coluna])

for linha in range(n_linhas):
    for coluna in range(n_colunas):
                print(matriz[linha][coluna], end=" ")
    print()