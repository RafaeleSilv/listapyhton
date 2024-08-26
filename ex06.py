# ) Escreva um algoritmo que lê dois valores booleanos (lógicos) e então determina se ambos são VERDADEIROS ou FALSOS.

valor1 = input("Digite o primeiro valor booleano (True/False): ").strip().capitalize()
valor2 = input("Digite o segundo valor booleano (True/False): ").strip().capitalize()


valor1 = valor1 == "True"
valor2 = valor2 == "True"


if valor1 and valor2:
    print("Ambos os valores são VERDADEIROS.")
elif not valor1 and not valor2:
    print("Ambos os valores são FALSOS.")
else:
    print("Um dos valores é VERDADEIRO e o outro é FALSO.")
