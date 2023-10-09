import os

def imprimir_numero(numero):
  os.system('cls' if os.name == 'nt' else 'clear')
  print(numero)

numero = 0

while numero <= 50:
  imprimir_numero(numero)
  numero += 1
