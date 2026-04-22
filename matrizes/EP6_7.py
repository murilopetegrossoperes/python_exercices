#Nesta atividade, o objetivo é implementar uma função ou método que construa e retorne uma matriz quadrada de ordem n (onde n é ímpar). A matriz deve desenhar um "X" usando o número 1 nas diagonais e 0 nas demais posições.
def obter_matriz_x(n):
    n_linhas = n
    n_colunas = n
    
    matriz = [[0 for c in range(n_colunas)] for l in range(n_linhas)]
    for i in range(n_linhas):
        for j in range(n_colunas):
            if i == j or i + j == (n - 1):
                matriz[i][j] = 1
    return matriz