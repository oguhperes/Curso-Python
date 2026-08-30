# Ler ano de nascimento de uma pessoa e informar conforma a idade:
# Se ele vai se alistar futuramente, se é a hora de se alistar, se ja passou do tempo de se alistar, mostrar também o tempo
# que falta ou passou do prazo

from datetime import date

try:
    print(' \n--- Consultar seu status de serviço militar --- ')
    ano = int(input('Em que ano você nasceu? '))
    ano_atual = date.today().year
    idade = ano_atual - ano
    

    if ano > ano_atual:
        print('Digite um ano válido! ') 

    else:

        if idade < 18:
            anos_faltando = 18 - idade
            print(f'Você não precisa se alistar! Faltam {anos_faltando} Ano(s) para você se alistar ')

        elif idade == 18:
            print('Está na hora de se alistar! Acesse o site https://alistamento.eb.mil.br/')

        else:
            anos_passados_do_prazo = idade - 18
            print(f'Já passou a hora de se alistar! Você está {anos_passados_do_prazo} Ano(s) atrasado ')
        

except ValueError:
    print('Digite um número válido! ')

