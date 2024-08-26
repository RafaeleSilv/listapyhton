# Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos). 

nome = str(input('digite seu nome: '))
sexo = str(input('digite seu sexo(F para feminino e M para masculino): '))
estadoc = str(input('digite seu estado civil: '))

if sexo == 'F' and estadoc == 'CASADA' :
    input('Por favor, me informe o tempo de casada:')
    print('Obrigada pelas informações!')
    
else :
    print('Obrigada pelas informações!')
    