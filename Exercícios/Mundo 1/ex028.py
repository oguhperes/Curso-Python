# Aumento salarial, salario superior a 1250 aumento de 10%, para inferiores ou iguais aumento de 15%

try:
    print(' --- Descubra o seu aumento --- ')
    salario = float(input('Seu salário: '))
    if salario > 1250:
        aumento1 = salario * 0.1
        novo_salario = salario + aumento1
        print(f'Seu novo salário é R$ {novo_salario:.2f} ')

    else:
        aumento2 = salario * 0.15
        novo_salario2 = salario + aumento2
        print(f'Seu nofo salário é R$ {novo_salario2:.2f}')

except ValueError:
    print('Digite um número válido! ')
        
