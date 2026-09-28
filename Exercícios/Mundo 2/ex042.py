# Calcular a soma entre todos os números ímpares que são multiplos de três
# e que se encontram no intervalo de 1 até 500

soma = 0

for numero in range(1, 500, 2):
    if numero % 3 == 0:
        soma += numero
print(soma)
