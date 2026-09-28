# Aumento salarial, salario superior a 1250 aumento de 10%, para inferiores ou iguais aumento de 15%

try:
    print(' \n--- Descubra o seu aumento --- ')
    salario = float(input('Seu salário: '))
    porcentagem = 0.1 if salario > 1250 else 0.15
    aumento = salario * porcentagem
    salario_final = salario + aumento

    print(f'Seu salário era R$ {salario:.2f} e vai ficar R$ {salario_final:.2f}')
except ValueError:
    print('Digite um número válido! ')
        
