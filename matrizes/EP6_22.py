#O desafio agora consiste em extrair informações específicas de uma matriz quadrada de tamanho 3 X 3. Você deve calcular a soma dos elementos que atravessam a estrutura em ambas as direções diagonais.
soma_principal = 0
soma_secundaria = 0
n_linhas = 3
n_colunas = 3


matriz = [[0 for c in range(n_colunas)] for l in range(n_linhas)]

for linha in range(n_linhas):
    for coluna in range(n_colunas):
        matriz[linha][coluna] = int(input())

for i in range(n_linhas):
    for j in range(n_colunas):
        if i == j:
            soma_principal += matriz[i][j]

for i in range(n_linhas):
    for j in range(n_colunas):
        if i + j == n_colunas - 1:
            soma_secundaria += matriz[i][j]

print(f"Soma diagonal principal: {soma_principal}")
print(f"Soma diagonal secundaria: {soma_secundaria}")

for i in range(n_linhas):
    for j in range(n_colunas):
             print(matriz[i][j], end=" ")
    print()
