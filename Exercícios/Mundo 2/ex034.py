# Leia duas notas e calcule a média, média abaixo de 5: Reprovado;
# Média entre 5 e 6.9 Recuperação; Média igual ou superior a 7 Aprovado

while True:
    try:
        print(' \n--- Situação escolar --- ')
        n1 = float(input('Primeira nota: '))
        n2 = float(input('Segunda nota: '))
        
        if n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10:
            print('Digite sua real nota! ')
            continue

        media = (n1 + n2) / 2

        if media < 5:
            print(f'Você foi reprovado! Sua média foi {media:.1f}')

        elif media <= 6.9:
            print(f'Você está de recuperação! Sua média foi {media:.1f}')

        else:
            print(f'Parabéns, você foi aprovado! Sua média foi {media:.1f}')

        break

    except ValueError:
        print('Digite um número válido! ')