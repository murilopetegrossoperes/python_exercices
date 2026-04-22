#Seu objetivo é processar uma matriz de tamanho fixo 3 X 3, preenchida com números inteiros distintos. O sistema deve identificar não apenas os valores limites, mas exatamente onde eles se encontram na estrutura.

n_linhas = 3
n_colunas = 3
maior = 0
menor = 0
posicao_maior = (0, 0)
posicao_menor = (0, 0)

matriz = [[0 for c in range(n_colunas)] for l in range(n_linhas)]

for linha in range(n_linhas):
    for coluna in range(n_colunas):
        valor = int(input())
        matriz[linha][coluna] = valor

        if linha == 0 and coluna == 0:
            maior = valor
            menor = valor
            posicao_maior = (linha, coluna)
            posicao_menor = (linha, coluna)
        else:
            if valor > maior:
                maior = valor
                posicao_maior = (linha, coluna)
            if valor < menor:
                menor = valor
                posicao_menor = (linha, coluna)

print(f"Maior: {maior}")
print(f"Posicao (maior): {posicao_maior[0]} linha e {posicao_maior[1]} coluna")
print(f"Menor: {menor}")
print(f"Posicao (menor): {posicao_menor[0]} linha e {posicao_menor[1]} coluna")


for i in range(n_linhas):
    for j in range(n_colunas):
             print(matriz[i][j], end=" ")
    print()
