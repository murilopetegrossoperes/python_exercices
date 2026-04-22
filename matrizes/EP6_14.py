#você deve processar uma matriz quadrada de ordem n e calcular a soma de todos os elementos localizados na região acima da diagonal principal.
n =  int(input())
n_linhas = n
n_colunas = n
soma = 0
matriz = [[0 for c in range(n_colunas)] for l in range(n_linhas)]

for linha in range(n_linhas):
    for coluna in range(n_colunas):
        matriz[linha][coluna] = int(input())

for i in range(n_linhas):
    for j in range(i+1, n_colunas):
        soma += matriz[i][j]
print(f"A soma eh: {soma}")