#o desafio é simular o processo de "dobrar" uma matriz quadrada de dimensão n×n(onde é par). A dobra ocorre em duas etapas: primeiro na horizontal e depois na vertical, resultando em uma matriz final de tamanho (n/2)×(n/2)

n =  int(input())
n_linhas = n
n_colunas = n

matriz = [[0 for c in range(n_colunas)] for l in range(n_linhas)]
for linha in range(n_linhas):
    itens_linha = input().split(" ")
    for coluna in range(n_colunas):
        matriz[linha][coluna] = int(itens_linha[coluna])


metade = n // 2
matriz_dobrada_h = [[0 for m in range(n)] for m in range(metade)]

for i in range(metade):
    for j in range(n):
        matriz_dobrada_h[i][j] = matriz[i][j] + matriz[n - 1 - i][j]


matriz_final = [[0 for m in range(metade)] for m in range(metade)]

for i in range(metade):
    for j in range(metade):
        matriz_final[i][j] = matriz_dobrada_h[i][j] + matriz_dobrada_h[i][n - 1 - j]


for i in range(metade):
      for j in range(metade):
            print(matriz_final[i][j], end=" ")
      print()
