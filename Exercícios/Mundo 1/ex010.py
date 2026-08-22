
# Aumento de salario de funcionario, 15%

try:
    salario = float(input('Digite seu salário: R$ '))
    aum = salario * 0.15
    valor = salario + aum

    print(f'Seu salário era de R$ {salario:.2f} e agora é R$ {valor:.2f}')

except ValueError:
    print('Digite um número válido! ')