def ler_e_dilatar_PBM(filename):
    with open(filename, 'r') as file: 
        lines = file.readlines()

    if lines[0].strip() != 'P1':
        raise ValueError('O arquivo não é uma imagem PBM válida.')
    
    vet = lines[1].split() 
    width = int(vet[0])
    height = int(vet[1])
    print(filename)
    print(lines[0].strip())
    print(width, height)

    linhas_texto = [""] * height
    
    for i in range(height):
        row = lines[i + 2].strip() 
        linhas_texto[i] = row
        
    for i in range(height):
        print(linhas_texto[i])

    pixels = [[0]*width for _ in range(height)]
    
    for i in range(height):
        row = lines[i + 2].strip() 
        for j in range(len(row)):
            pixels[i][j] = int(row[j])

    linhas = len(pixels)
    colunas = len(pixels[0])

    nova_matriz = [[0 for _ in range(colunas)] for _ in range(linhas)]

    deslocamentos = [-1, 0, 1]

    for i in range(linhas):
        for j in range(colunas):
            
            if pixels[i][j] == 1:
                nova_matriz[i][j] = 1

                for idx_i in range(3):
                    for idx_j in range(3):
                        di = deslocamentos[idx_i]
                        dj = deslocamentos[idx_j]
                        ni, nj = i + di, j + dj
                        
                        if 0 <= ni and ni < linhas and 0 <= nj and nj < colunas:
                            nova_matriz[ni][nj] = 1
    
    print("\nMatriz Resultante")                    
    
    nova_linhas_texto = [""] * linhas
    
    for i in range(linhas):
        row_str = ""
        for j in range(colunas):
            row_str += str(nova_matriz[i][j])
        
        nova_linhas_texto[i] = row_str
    
    for i in range(linhas):
        print(nova_linhas_texto[i])
        
arquivo = input("")
matriz_final = ler_e_dilatar_PBM(arquivo)