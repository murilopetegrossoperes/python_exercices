#Nesta tarefa, você deve ler uma matriz quadrada 3×3 de números inteiros. O objetivo é condensar essa estrutura em um vetor (array) de 3 posições, onde cada elemento do vetor corresponda à soma total de uma coluna específica da matriz.

n_linhas = 3
n_colunas = 3
soma_principal = 0

matriz = [[0 for c in range(n_colunas)] for l in range(n_linhas)]
vetor_soma_colunas = [0 for c in range(n_colunas)]


for linha in range(n_linhas):
    for coluna in range(n_colunas):
        matriz[linha][coluna] = int(input())
        vetor_soma_colunas[coluna] += matriz[linha][coluna]

print("Vetor soma colunas:")
for elemento in vetor_soma_colunas:
    print(elemento, end=" ")
print()
