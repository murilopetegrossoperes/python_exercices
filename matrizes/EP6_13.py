#você deve construir uma matriz de dimensões n_linhas×n_colunas preenchida com uma sequência de números pares, começando pelo zero. O grande diferencial é que o preenchimento deve ser feito coluna por coluna.
n_linhas = int(input())
n_colunas = int(input())
soma = 0

matriz = [[0 for c in range(n_colunas)] for l in range(n_linhas)]

for coluna in range(n_colunas):
    for linha in range(n_linhas):
        matriz[linha][coluna] = soma
        soma += 2

for i in range(n_linhas):
    for j in range(n_colunas):
        print(matriz[i][j], end=" ")
    print() 