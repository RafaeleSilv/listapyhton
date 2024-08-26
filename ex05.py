# Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo,imprimindo o resultado.

n = float(input('digite um número: '))

if n > 0 :
    d = n * 2
    print('o dobro de {} é {}'.format(n,d))
    
else :
    t = n * 3
    print('o triplo de {} é {}'.format(n,t))
