def calcular_consumo(distancia, litros):
	return distancia / litros

def calcular_consumo_medio(viagens):
	total_distancia = 0
	total_litros = 0
	consumos = []

	for viagem in viagens:
		distancia, litros = viagem
		consumo = calcular_consumo(distancia, litros)
		consumos.append(consumo)
		total_distancia = total_distancia + distancia
		total_litros = total_litros + litros

	consumo_medio_total = calcular_consumo(total_distancia, total_litros)
	return consumos, consumo_medio_total

def main():
	viagens = []
	while True:
		distancia = float(input("Digite a distância percorrida (ou 0 para sair): "))
		if distancia == 0:
			break
		litros = float(input("Digite a quantidade de litros consumidos: "))
		print("\n")
		viagens.append((distancia, litros))

	consumos, consumo_medio_total = calcular_consumo_medio(viagens)
    
	for i, consumo in enumerate(consumos):
		print(f"Consumo médio da viagem {i + 1}: {consumo:.2f}km/l")

	print(f"\nConsumo médio total de todas as viagens: {consumo_medio_total:.2f}km/l")

main()