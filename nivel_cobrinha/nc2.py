def maior_valor(primeiro, segundo, terceiro):
    lista_numeros = [primeiro, segundo, terceiro]
    maior_valor = max(primeiro, segundo, terceiro)

    lista_numeros.sort()
    print(f"Maior valor: {maior_valor}")
    print(f"Lista ordenada: {lista_numeros}")

primeiro = float(input("Digite o primeiro número: "))
segundo = float(input("Digite o segundo número: "))
terceiro = float(input("Digite o terceiro número: "))

maior_valor(primeiro, segundo, terceiro)