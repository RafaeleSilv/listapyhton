# Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem decrescente

n1 = int(input('digite o primeiro número: '))
n2 = int(input('digite o segundo número:  '))
n3 = int(input('digite o terceiro número: '))

lista = [n1, n2, n3]
print(sorted(lista, reverse=True))
