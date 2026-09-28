# Ler ano de nascimento de uma pessoa e informar conforma a idade:
# Se ele vai se alistar futuramente, se é a hora de se alistar, se ja passou do tempo de se alistar, mostrar também o tempo
# que falta ou passou do prazo

from datetime import date

while True:
    try:
        print(' \n--- Consultar seu status de serviço militar --- ')
        ano_de_nascimento = int(input('Ano de nascimento: '))
        ano_atual = date.today().year
        if ano_de_nascimento > ano_atual:
            print('Digite um ano válido! ')
            continue
        else:
            idade = ano_atual - ano_de_nascimento

            if idade < 18:
                anos_faltando = 18 - (ano_atual - ano_de_nascimento)
                print(f'Você tem {idade} anos! Falta {anos_faltando} Ano(s) para você se alistar')

            elif idade == 18:
                print(f'Você tem {idade} Anos. Está na hora de se alistar!!! ')

            elif idade > 18:
                anos_sobrando = (ano_atual -ano_de_nascimento) - 18
                print(f'Já passou do tempo de se alistar. Passou {anos_sobrando} Ano(s)!!! ')
            break

            

    except ValueError:
        print('Digite um número válido! ')

