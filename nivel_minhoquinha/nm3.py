def calcular_media(lista_numeros):
  soma = 0
  for numero in lista_numeros:
    soma = soma + numero
  media = soma / len(lista_numeros)
  return media

minha_lista = [25, 42, 24, 71, 22]
media_resultado = calcular_media(minha_lista)
print("A média dos números é:", media_resultado)