#O desafio agora é construir uma matriz quadrada de tamanho n X n onde os valores não são lidos, mas sim gerados logicamente com base em suas posições. O valor da posição (i, j) deve ser igual a i + j + 1. Lembre-se que as posições começam a ser contadas a partir do zero.
n =  int(input())
n_linhas = n
n_colunas = n
t = 0
matriz = [[0 for c in range(n_colunas)] for l in range(n_linhas)]

for linha in range(n_linhas):
    t = linha
    for coluna in range(n_colunas):
        matriz[linha][coluna] = (t+1)
        t += 1

for i in range(n_linhas):
    for j in range(n_colunas):
             print(matriz[i][j], end=" ")
    print()
