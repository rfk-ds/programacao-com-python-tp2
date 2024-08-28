valor_inicial = float(input("Digite o valor inicial: "))
taxa_juros = float(input("Digite a taxa de juros anual: "))
tempo = int(input("Digite o tempo em anos: "))

def calcular_valor_final(valor_inicial, taxa_juros, tempo):
    valores_anuais = []
    for ano in range(1, tempo + 1):
        valor_final = valor_inicial * (1 + taxa_juros/100) ** ano
        valores_anuais.append(valor_final)
    return valores_anuais

valores_anuais = calcular_valor_final(valor_inicial, taxa_juros, tempo)

for ano, valor in enumerate(valores_anuais, 1):
    print(f"Ao final do ano {ano}, o valor é {valor:.2f}")