#você deve validar se uma matriz atende a dois critérios simultâneos: todos os seus elementos devem ser múltiplos de 10 e cada uma de suas linhas deve estar individualmente ordenada (seja de forma crescente ou decrescente).
n_linhas = int(input())
n_colunas = int(input())
erro = 0

matriz = [[0 for c in range(n_colunas)] for l in range(n_linhas)]

for linha in range(n_linhas):
    itens_linha = input().split(" ")


    for coluna in range(n_colunas):
        matriz[linha][coluna] = int(itens_linha[coluna])
        if matriz[linha][coluna] % 10 != 0:
            erro = 1

    crescente = 1
    decrescente = 1
    anterior = matriz[linha][0]
    
    for coluna in range(1, n_colunas):
        atual = matriz[linha][coluna]
        
        if atual >= anterior:
            decrescente = 0  
        elif atual <= anterior:
            crescente = 0    

        anterior = atual


    if crescente == 0 and decrescente == 0:
        erro = 1

if erro == 1:
    print("NAO")
else:
    print("SIM")