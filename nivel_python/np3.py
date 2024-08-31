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
        
        input_usuario = input("Digite 'fim' para encerrar ou pressione enter para prosseguir: ").lower()
        if input_usuario == "fim":
            break
        else:
            continue

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


def verificar_intervalo_seguranca(media_ponderada):
    if 20 <= media_ponderada <= 30:
        print(f"A média ponderada das temperaturas ({media_ponderada:.1f}°C) está dentro do intervalo de segurança (20°C a 30°C).")
    else:
        print(f"A média ponderada das temperaturas ({media_ponderada:.1f}°C) está fora do intervalo de segurança (20°C a 30°C).")


def encontrar_temperaturas_extremas(lista_horarios, lista_temperaturas):
    min_temp = min(lista_temperaturas)
    max_temp = max(lista_temperaturas)
    hora_min_temp = lista_horarios[lista_temperaturas.index(min_temp)]
    hora_max_temp = lista_horarios[lista_temperaturas.index(max_temp)]

    print(f"A temperatura mais baixa foi {min_temp}°C registrada às {hora_min_temp}h.")
    print(f"A temperatura mais alta foi {max_temp}°C registrada às {hora_max_temp}h.")

def main():
    lista_horarios, lista_temperaturas = entrada_dados()
    media_ponderada = calcular_media_ponderada(lista_horarios, lista_temperaturas)

    if media_ponderada is not None:
        verificar_intervalo_seguranca(media_ponderada)
        encontrar_temperaturas_extremas(lista_horarios, lista_temperaturas)

main()