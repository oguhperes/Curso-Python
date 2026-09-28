# Leia duas notas e calcule a média, média abaixo de 5: Reprovado;
# Média entre 5 e 6.9 Recuperação; Média igual ou superior a 7 Aprovado

while True:
    try:
        print(' \n--- Situação escolar --- ')
        n1 = float(input('Primeira nota: '))
        n2 = float(input('Segunda nota: '))
        media = (n1 + n2) / 2
        if media < 5:
            print(f'Sua média foi {media}. Você está reprovado!!! ')
        elif media <= 6.9:
            print(f'Sua média foi {media}. Você está de recuperação!!! ')
        else:
            print(f'Sua média foi {media}. Você está aprovado !!!')
        break 
    
    except ValueError:
        print('Digite um número válido! ')