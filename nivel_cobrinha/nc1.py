def potencia(base, expoente = 2):
    calculo = base ** expoente
    return calculo

def teste():
    teste1 = potencia(5)
    teste2 = potencia(5, 3)
    print(teste1)
    print(teste2)

teste()