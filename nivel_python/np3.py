def entrada_dados():
    lista_horarios = []
    lista_temperaturas = []

    while True:
        try:
            hora_registro = int(input("Digite a hora do registro: "))
            if hora_registro < 0 or hora_registro > 23:
                print("Digite um número entre 0 e 23")
            else:
                lista_horarios.append(hora_registro)
        except ValueError:
            print("Digite um número inteiro")
        
        try:
            temperatura = float(input("Digite a temperatura: "))
            if temperatura < -15 or temperatura > 60:
                print("Digite um número entre -15 e 60")
            else:
                lista_temperaturas.append(temperatura)
        except ValueError:
            print("Digite um número real")
        
        input_usuario = input("Deseja continuar? (s/n): ")
        if input_usuario == "s":
            continue
        elif input_usuario == "n":
            break
        else:
            print("Digite 's' para continuar ou 'n' para sair")

    return lista_horarios, lista_temperaturas

def calcular_media_ponderada(lista_horarios, lista_temperaturas):
    total_peso = 0
    soma_ponderada = 0

    for i in range(1, len(lista_horarios)):
        intervalo = lista_horarios[i] - lista_horarios[i - 1]
        if intervalo < 0:
            intervalo += 24
        peso = intervalo
        total_peso += peso
        soma_ponderada += lista_temperaturas[i - 1] * peso

    media_ponderada = soma_ponderada / total_peso
    return media_ponderada