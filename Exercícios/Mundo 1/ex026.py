# Calcular se ano é Bissexto

while True:
    try:
        print('\nO ano é Bissexto? ')
        ano = int(input('Digite o ano: '))
        if ano < 0:
            print('Digite um ano válido! ')
            continue
        else:
            if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
                print(f'O ano {ano} é Bissexto! ')
            else:
                print(f'O ano {ano} não é Bissexto')
            break
    except ValueError:
        print('Digite um número válido! ')
        


