def criar_lista_caracteres(entrada):
    lista_caracteres = []

    for caractere in entrada:
        lista_caracteres.append(caractere)
    return lista_caracteres
    
entrada = input("Digite uma string: ")
saida = criar_lista_caracteres(entrada)
print(saida)