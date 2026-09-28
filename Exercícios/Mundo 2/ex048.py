# Ler o ano de nascimento de sete pessoas
# No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores

from datetime import date


try:
    contador_menores = 0
    contador_maiores = 0
    verificacao = date.today().year - 17
    for ano in range(1, 8):
        ano_nascimento = int(input(f'{ano} - Ano de nascimento: '))
        if ano_nascimento >= verificacao:
            contador_menores += 1
        else:
            contador_maiores += 1
    if contador_maiores == 1:
        print('Desses anos apenas 1 pessoa é maior de idade e 6 são menores de idade!!! ')
    elif contador_menores == 1:
        print('Desses anos apenas 1 pessoa é menor de idade e 6 são maiores de idade!!! ')
    else:
        print(f'Desses anos {contador_menores} pessoas são menores de idade e {contador_maiores} são maiores de idade!!! ')
        
except ValueError:
    print('Digite um número válido! ')