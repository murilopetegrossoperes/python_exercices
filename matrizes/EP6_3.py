#o objetivo é implementar uma função ou método que verifique uma relação específica entre duas matrizes: a matriz2 deve possuir exatamente o dobro do valor da matriz1 em cada posição correspondente.

def comparar_matrizes(matriz1, matriz2):
    if len(matriz1) != len(matriz2):
        return False
    
    for i in range(len(matriz1)):
        if len(matriz1[i]) != len(matriz2[i]):
            return False
        
        for j in range(len(matriz1[i])):
            if matriz1[i][j] * 2 != matriz2[i][j]:
                return False
                
    return True