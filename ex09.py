h = float(input('digite a sua altura: '))
sexo = str(input('digite seu sexo (M/F): '))

if sexo == 'F' :
    imc = (62.1 * h) - 44.7
    print('seu peso ideal é: {}'.format(imc))
else :
    imc = (72.7 * h) -58
    print('seu peso ideal é: {:.2f}'.format(imc))