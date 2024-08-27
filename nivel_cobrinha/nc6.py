def gerar_lista_pares(n):
    lista_pares = []
    for i in range(n + 1):
        if i % 2 == 0:
            lista_pares.append(i)
    return lista_pares

n = int(input("Digite até onde deseja gerar a lista de pares: "))
print(gerar_lista_pares(n))