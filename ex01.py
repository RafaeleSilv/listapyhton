# Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C

a = int(input('digite o valor de A: '))
b = int(input('digite o valor de B: '))
c = int(input('digite o valor de C: '))

if a + b < c :
    
    print('A SOMA DE {} + {} É MENOR QUE {}'.format(a, b, c))
    
else :
    
    print('A SOMA DE {} + {} É MAIOR QUE {}'.format(a, b, c))
