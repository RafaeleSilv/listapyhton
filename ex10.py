# O IMC – Indice de Massa Corporal é um critério da Organização Mundial de Saúde para dar umaindicação sobre a condição de peso de uma pessoa adulta. A fórmula é IMC = peso / ( altura )2

# Elabore um algoritmo que leia o peso e a altura de um adulto e mostre sua condição de acordo com a tabela abaixo


peso = float(input('digite seu peso: '))
h = float(input('digite sua altura: '))
imc = peso / (h**2)

print('seu imc é: {:.2f}' .format(imc))
if imc < 18.5 :
    print('abaixo do peso')
elif imc >= 18.5 and imc <=25 :
    print('Peso Normal')
elif imc >=25 and imc <=30 :
    print('Acima do peso')
else :
    print('OBESO!!!')