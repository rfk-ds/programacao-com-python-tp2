def saudacao(nome):
    if nome == "":
        print("Olá, pessoa!")
    else:
        print(f"Olá, {nome}!")

nome = input("Digite seu nome: ")
saudacao(nome)