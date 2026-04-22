# Pega uma matriz de inteiros e imprime a matriz resultante da multiplicação por 3 dos elementos que estão nas colunas ímpares (1, 3, 5, etc.). Os elementos das colunas pares (0, 2, 4, etc.) devem ser impressos sem alteração.
n_linhas = int(input())
n_colunas = int(input())

matriz = [[0 for c in range(n_colunas)] for l in range(n_linhas)]

for linha in range(n_linhas):
    itens_linha = input().split(" ")

    for coluna in range(n_colunas):
        matriz[linha][coluna] = int(itens_linha[coluna])

for linha in range(n_linhas):
    for coluna in range(n_colunas):
            if coluna % 2 == 1:
                print(matriz[linha][coluna]*3, end=" ")
            else:                
                print(matriz[linha][coluna], end=" ")
    print()
