# Usando a mesma implementação da questão 5 modifique a função para que, caso nenhum argumento seja passado, exiba uma saudação genérica.

def saudacao(nome):
    if nome == "":
        print("Olá, pessoa!")
    else:
        print(f"Olá, {nome}!")

nome = input("Digite seu nome: ")
saudacao(nome)