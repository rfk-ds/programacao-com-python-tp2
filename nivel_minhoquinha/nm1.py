# Crie um programa que receba uma string como entrada do usuário e use um loop for para criar uma lista com cada caractere da string. 

def criar_lista_caracteres(entrada):
    lista_caracteres = []

    for caractere in entrada:
        lista_caracteres.append(caractere)
    return lista_caracteres
    
entrada = input("Digite uma string: ")
saida = criar_lista_caracteres(entrada)
print(saida)