# Você deve processar uma matriz quadrada de dimensão n×n e calcular o produto acumulado de todos os elementos que compõem a sua diagonal secundária.

n =  int(input())
n_linhas = n
n_colunas = n
soma = 0
matriz = [[0 for c in range(n_colunas)] for l in range(n_linhas)]

for linha in range(n_linhas):
    for coluna in range(n_colunas):
        itens_linha = int(input())
        matriz[linha][coluna] = int(itens_linha)

for i in range(n_linhas):
    for j in range(n_colunas):
        if i + j == n - 1:
            if soma != 0: 
                soma = matriz[i][j]*soma 
            else: 
                soma = matriz[i][j]

print(f"O produto eh: {soma}")