#  Faça um algoritmo para receber um número qualquer e informar na tela se é par ou ímpar.

n = int(input('digite um número: '))

if n % 2 == 0 :
    print('{} é par!'.format(n))

else :
    print('{} é ímpar!'.format(n))