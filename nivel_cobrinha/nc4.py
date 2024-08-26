def potencia(base, expoente = 2):
    """
    Calcula base elevada ao expoente

    Args:
    base(int | float): primeiro número a ser considerado
    expoente(int | float): segundo número a ser considerado

    Expoente começa com o valor padrão 2

    Return:
    (int | float): Resultado do cálculo
    """
    calculo = base ** expoente
    return calculo

teste1 = potencia(5)
teste2 = potencia(5, 3)
print(f"Resultado: {teste1}")
print(f"Resultado: {teste2}")

print("\n")

def maior_valor(primeiro, segundo, terceiro):
    """
    Determina o maior valor entre três números e ordena os valores em ordem crescente.

    Args:
    primeiro (float): O primeiro número.
    segundo (float): O segundo número.
    terceiro (float): O terceiro número.

    Retorna:
    Nada: Esta função não retorna um valor, mas imprime o maior valor e a lista ordenada dos números.

    Exibe:
    Maior valor (float): O maior valor entre os três números fornecidos.
    Lista ordenada (list): Os três números fornecidos em ordem crescente.
    """

    lista_numeros = [primeiro, segundo, terceiro]

    maior_valor = max(primeiro, segundo, terceiro)

    lista_numeros.sort()

    print(f"Maior valor: {maior_valor}")
    print(f"Lista ordenada: {lista_numeros}")

primeiro = float(input("Digite o primeiro número: "))
segundo = float(input("Digite o segundo número: "))
terceiro = float(input("Digite o terceiro número: "))

maior_valor(primeiro, segundo, terceiro)

print("\n")

def imprime_dados(nome, preco, quantidade):
    """
    Imprime os dados de um produto.

    Args:
    nome (str): O nome do produto.
    preco (float): O preço do produto.
    quantidade (int): A quantidade disponível do produto.

    Retorna:
    Nada
    """
    print(f"Nome: {nome}")
    print(f"Preço: {preco}")
    print(f"Quantidade: {quantidade}")

nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))

imprime_dados(nome, preco, quantidade)