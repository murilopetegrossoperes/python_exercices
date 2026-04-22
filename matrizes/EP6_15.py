# Função para somar os vizinhos de um elemento em uma matriz

def somar_vizinhos(matriz, linha, coluna):
    soma = 0 
    linhas = len(matriz)
    colunas = len(matriz[0])

    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue 
            
            ni, nj = linha + di, coluna + dj 
            
            if 0 <= ni < linhas and 0 <= nj < colunas:
                soma += matriz[ni][nj]
    return soma
