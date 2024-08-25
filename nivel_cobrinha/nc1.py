# Defina uma função chamada potencia que receba dois números como argumento, a base e o expoente. O expoente deve ter um valor padrão de 2. A função deve calcular e retornar a base elevada ao expoente.

def potencia(base, expoente = 2):
    calculo = base ** expoente
    return calculo

def teste():
    teste1 = potencia(5)
    teste2 = potencia(5, 3)
    print(teste1)
    print(teste2)

teste()