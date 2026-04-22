#você deve processar uma matriz de notas onde cada linha representa um aluno e cada coluna uma de suas notas. O objetivo é calcular a média de cada aluno e expandir a matriz, adicionando essa média em uma nova coluna ao final.
n_linhas = int(input())
n_colunas = int(input())
soma = 0

matriz = [[0 for c in range(n_colunas)] for l in range(n_linhas)]

for linha in range(n_linhas):
    itens_linha = input().split(" ")
    for coluna in range(n_colunas):
        matriz[linha][coluna] = float(itens_linha[coluna])


for i in range(n_linhas):
    soma = 0
    for j in range(n_colunas):
      print("%.2f" % matriz[i][j], end=" ")
      soma += matriz[i][j]

    media = soma / (n_colunas)
    print("%.2f" % media, end="")
    print()