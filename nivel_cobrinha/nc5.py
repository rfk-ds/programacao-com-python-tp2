def exibir_mensagem(mensagem, repeticoes = 1):
    for _ in range(repeticoes):
        print(mensagem)

mensagem = input("Digite a mensagem: ")
repeticoes = int(input("Digite o número de repetições: "))
exibir_mensagem(mensagem, repeticoes)