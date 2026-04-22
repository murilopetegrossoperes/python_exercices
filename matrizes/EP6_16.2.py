def ler_e_dilatar_PBM(filename):
    # ==========================================
    # PARTE 1: LEITURA DO ARQUIVO
    # ==========================================
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
        row = lines[i].strip() 
        linhas_texto.append(row)
        
    for j in linhas_texto:
        print(j)

    pixels = [[0]*width for _ in range(height)]
    
    for i in range(2, height + 2):
        row = lines[i].strip() 
        for j in range(len(row)):
            pixels[i-2][j] = int(row[j])


    # ==========================================
    # PARTE 2: DILATAÇÃO DA MATRIZ
    # ==========================================
    linhas = len(pixels)
    colunas = len(pixels[0])

    nova_matriz = [[0 for _ in range(colunas)] for _ in range(linhas)]

    for i in range(linhas):
        for j in range(colunas):
            
            if pixels[i][j] == 1:
                nova_matriz[i][j] = 1

                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        ni, nj = i + di, j + dj
                        
                        if 0 <= ni < linhas and 0 <= nj < colunas:
                            nova_matriz[ni][nj] = 1
    
    print("\nMatriz Resultante")                    
    nova_linhas_texto = []
# Passamos por cada linha diretamente da nova_matriz
    for linha in nova_matriz:
    
    # Transformamos a lista [0, 0, 1, 1] no texto "0011"
        row = "".join(str(pixel) for pixel in linha)
    
    # Guardamos o texto na nova lista
        nova_linhas_texto.append(row)
    
# Por fim, imprimimos linha por linha
    for j in nova_linhas_texto:
     print(j)


# Chamando a nova função unificada
arquivo = 'imagem1.pbm'
matriz_final = ler_e_dilatar_PBM(arquivo)