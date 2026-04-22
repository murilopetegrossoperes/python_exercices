#Escreva um programa que leia uma matriz contendo o mapa de um campo minado (1 para bomba, 0 para vazio). Exemplo de mapa:
n_linhas, n_colunas = input().split(" ")
n_linhas = int(n_linhas)
n_colunas = int(n_colunas)

matriz = [[0 for c in range(n_colunas)] for l in range(n_linhas)]

for linha in range(n_linhas):
    itens_linha = input().split(" ")

    for coluna in range(n_colunas):
        matriz[linha][coluna] = int(itens_linha[coluna])


i, j = input().split(" ")
i = int(i)
j = int(j)

def obter_vizinhos(matriz, i, j):

    soma = 0 
    linhas = len(matriz)
    colunas = len(matriz[0])

    # Percorre de -1 a 1 para linha e coluna
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue # Pula o elemento central
            
            ni, nj = i + di, j + dj # Novo índice

            # Verifica se o vizinho está dentro dos limites
            if 0 <= ni < linhas and 0 <= nj < colunas:
                soma += matriz[ni][nj]
    return soma

soma = obter_vizinhos(matriz, i, j)
print(soma)