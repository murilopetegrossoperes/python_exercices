def leiaImagemPBM(filename):
    with open(filename, 'r') as file: 
        lines = file.readlines()

    if lines[0].strip() != 'P1':
        raise ValueError('O arquivo não é uma imagem PBM válida.')
    
    vet = lines[1].split() 
    width, height = [int(vet[i]) for i in range(len(vet))] 
    print(lines[0].strip())
    print(width, height)

    linhas_texto = []
    
    for i in range(2, height + 2):
        # O strip() pega a linha '00110\n' e transforma em '00110'
        row = lines[i].strip() 
        linhas_texto.append(row)
    for j in linhas_texto:
        print(j, end="")
        print()


    pixels = [[0]*width for _ in range(height)]
    for i in range(2,height+1):
        row = lines[i].strip() 
        for j in range(len(row)):
            pixels[i-2][j] = int(row[j])
    return pixels

arquivo = 'imagem1.pbm'
minha_matriz = leiaImagemPBM(arquivo)

def dilatar_imagem(matriz_pixels):
    linhas = len(matriz_pixels)
    colunas = len(matriz_pixels[0])

    # 1. Cria uma nova matriz de saída cheia de zeros (fundo escuro)
    nova_matriz = [[0 for _ in range(colunas)] for _ in range(linhas)]

    # 2. Percorre cada pixel da imagem original
    for i in range(linhas):
        for j in range(colunas):
            
            # 3. Se encontrarmos um pixel '1', espalhamos ele na NOVA matriz
            if matriz_pixels[i][j] == 1:
                
                # Garante que o centro também será 1 na nova matriz
                nova_matriz[i][j] = 1

                # O famoso "Radar" espalha o '1' para os 8 vizinhos
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        ni, nj = i + di, j + dj
                        
                        # Verifica se o vizinho não cai fora dos limites da imagem
                        if 0 <= ni < linhas and 0 <= nj < colunas:
                            # Transforma o vizinho em 1 na matriz de saída
                            nova_matriz[ni][nj] = 1

    # 4. Retorna a imagem processada
    return nova_matriz

imagem_dilatada = dilatar_imagem(minha_matriz)
print("\nMatriz Resultante")
for linha in imagem_dilatada:
    print(linha, end="")
    print()

    