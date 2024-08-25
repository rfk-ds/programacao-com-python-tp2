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