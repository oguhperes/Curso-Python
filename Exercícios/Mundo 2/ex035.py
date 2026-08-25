# Ler ano de nascimento e mostrar categoria de acordo com a idade:
# Até 9 anos: Mirim
# Até 14 anos: Infantil
# Até 19 anos: Junior 
# Até 20 anos: Sênior
# Acima: Master

from datetime import date

while True:
    try:
        print(' \n--- Verificar sua categoria --- ')
        ano_atual = date.today().year
        ano_nascimento = int(input('Qual seu ano de nascimento? '))

        if ano_nascimento > ano_atual:
            print('Digite um ano válido! ')
            continue

        idade = ano_atual - ano_nascimento

        if idade <= 9:
            print('Sua categoria é a Mirim! ')

        elif idade <= 14:
            print('Sua categoria é a Infantil! ')

        elif idade <= 19:
            print('Sua categoria é Junior')

        elif idade == 20:
            print('Sua categoria é Sênior! ')

        else:
            print('Sua categoria é Master!')

        break

    except ValueError:
        print('Digite um número válido! ')

