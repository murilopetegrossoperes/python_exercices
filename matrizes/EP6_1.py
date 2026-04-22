#você deve implementar um sistema de busca em uma grade de dados (matriz). O programa deve ler as dimensões da matriz, seus elementos e, por fim, localizar a posição de um número específico.

n_linhas = int(input())
n_colunas = int(input())
sinal = 0

matriz = [[0 for c in range(n_colunas)] for l in range(n_linhas)]

for linha in range(n_linhas):
    for coluna in range(n_colunas):
        matriz[linha][coluna] = int(input())

num_procurado= int(input())
for i in range(n_linhas):
    for j in range(n_colunas):
        if matriz[i][j] == num_procurado:
            print(i+1, j+1)
            sinal=1
            
if sinal != 1:
  print("-1") 