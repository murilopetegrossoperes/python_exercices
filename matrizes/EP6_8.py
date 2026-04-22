#você deve implementar um algoritmo que realize a multiplicação entre duas matrizes A e B e, em seguida, multiplique o resultado pelo escalar 3. A operação final desejada é 3×(A×B). O programa deve solicitar ao usuário as dimensões das matrizes A e B, bem como os elementos de cada matriz. Após realizar a multiplicação, o programa deve exibir a matriz resultante.
n_linhas_A = int(input())
n_colunas_A = int(input())
soma = 0

matriz_A = [[0 for c in range(n_colunas_A)] for l in range(n_linhas_A)]
for linha in range(n_linhas_A):
    itens_linha = input().split(" ")
    for coluna in range(n_colunas_A):
        matriz_A[linha][coluna] = int(itens_linha[coluna])


n_linhas_B = int(input())
n_colunas_B = int(input())

matriz_B = [[0 for c in range(n_colunas_B)] for l in range(n_linhas_B)]
for linha in range(n_linhas_B):
    itens_linha = input().split(" ")
    for coluna in range(n_colunas_B):
        matriz_B[linha][coluna] = int(itens_linha[coluna])


linhas_A = len(matriz_A)
colunas_A = len(matriz_A[0])
linhas_B = len(matriz_B)
colunas_B = len(matriz_B[0])

if colunas_A == linhas_B:
    R = [[0 for _ in range(colunas_B)] for _ in range(linhas_A)]

    for i in range(linhas_A):
        for j in range(colunas_B):
            soma_produto = 0
            for k in range(colunas_A):
                soma_produto += matriz_A[i][k] * matriz_B[k][j]
            R[i][j] = soma_produto

    for i in range(linhas_A):
        for j in range(colunas_B):
            R[i][j] = R[i][j] * 3

    for i in range(linhas_A):
      for j in range(colunas_B):
          print(R[i][j], end=" ")
      print()