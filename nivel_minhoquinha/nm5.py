# Crie uma função chamada saudacao imprima uma saudação personalizada, como "Olá, [nome do usuário]!", recebendo o nome como argumento da função.

def saudacao(nome):
    print(f"Olá, {nome}!")

nome = input("Digite seu nome: ")
saudacao(nome)