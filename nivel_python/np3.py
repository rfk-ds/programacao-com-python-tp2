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

    print(lista_horarios) 
    print(lista_temperaturas)

entrada_dados()