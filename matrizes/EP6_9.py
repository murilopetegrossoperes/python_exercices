#você deve elevar o nível da manipulação de dados: em vez de ler os valores do teclado, seu programa deve carregar duas matrizes a partir de arquivos externos no formato CSV e realizar a multiplicação entre elas.
def leiaMatrizCSV(nome_arquivo): 
    with open(nome_arquivo, "r") as arquivo:
        linhas = arquivo.read().split('\n')
    L = len(linhas) # Número de linhas 
    C = len(linhas[0].split(" ")) # Número de colunas
    m = [[0] * C for _ in range(L)]
    for i in range(L):
        linha = linhas[i].split(" ") # Dividindo a linha pelos →caracteresde espaço para obter os elementos individuais
        for j in range(C): # Verificando se há elementos suficientes na linha
            if len(linha) > j:
                m[i][j] = int(linha[j]) # Convertendo o elemento →parainteiro e atribuindo à matriz
    return m

input_fileA = input() # Substitua pelo nome do seu arquivo CSV
input_fileB = input() # Substitua pelo nome do seu arquivo CSV

print(input_fileA)
matrizA = leiaMatrizCSV(input_fileA)
for i in range(len(matrizA)):
    for j in range(len(matrizA[0])):
        print(matrizA[i][j], end=" ")
    print()
print() # Adiciona uma linha em branco entre as matrizes

print(input_fileB)
matrizB = leiaMatrizCSV(input_fileB)
for i in range(len(matrizB)):
    for j in range(len(matrizB[0])):
        print(matrizB[i][j], end=" ")
    print()
print() # Adiciona uma linha em branco entre as matrizes


linhas_A = len(matrizA)
colunas_A = len(matrizA[0])
linhas_B = len(matrizB)
colunas_B = len(matrizB[0])

if colunas_A == linhas_B:
    R = [[0 for _ in range(colunas_B)] for _ in range(linhas_A)]

    for i in range(linhas_A):
        for j in range(colunas_B):
            soma_produto = 0
            for k in range(colunas_A):
                soma_produto += matrizA[i][k] * matrizB[k][j]
            R[i][j] = soma_produto


    print("Matriz Resultante")

    for i in range(linhas_A):
      for j in range(colunas_B):
          print(R[i][j], end=" ")
      print()