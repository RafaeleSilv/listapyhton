# Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço normal deetiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir para ler qual acondição de pagamento escolhida e efetuar o cálculo adequado. 

produto = str(input('Qual produto você deseja comprar?: '))
preco = float(input('Qual o preço? : '))
mp = str(input('qual método de pagamento? \n A VISTA --> \n CARTÃO DE CRÉDITO --> \n PARCELADO 2X --> \n PARCELADO 3X --> \n :'))

if mp == 'A VISTA' :
    desconto = preco - (preco * 10 /100)
    print('o preço total ficou de R${}. Você teve um desconto de 10% '.format(desconto))
elif mp == 'CARTÃO DE CRÉDITO' :
    desconto = preco - (preco * 15 / 100)
    print('O preço total ficou de R${}. Você teve um desconto de 15%'.format(desconto))
elif mp == 'PARCELADO 3X' :
    juros = preco + (preco * 10 / 100)
    print('O valor total ficou de R${}. Teve um juros de 10%'.format(juros))
else :
    print('O valor total é de R${}. Não teve descontos ou juros.'.format(preco))