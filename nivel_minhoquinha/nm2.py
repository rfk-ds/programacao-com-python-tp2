# Crie um programa que peça ao usuário para inserir números um de cada vez até que ele digite 0. Armazene esses números em uma lista usando um loop while.

def listar_numeros():
    lista_numeros = []

    while True:
        entrada = int(input("Digite o número: "))
        if entrada == 0:
            break
        else:
            lista_numeros.append(entrada)
    
    print(lista_numeros)

listar_numeros()