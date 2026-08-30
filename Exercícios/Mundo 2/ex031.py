# Ler um número inteiro, usuário deve escolher qual conversão: 1- Binário, 2- Octal, 3- Hexadecimal

while True:
    try:
        print(' \n--- Conversão numeral --- ')
        n1 = int(input('Digite um número inteiro: '))
        print('\nEscolha uma opção: ')
        print('1- Binário ')
        print('2- Octal ')
        print('3- Hexadecimal ')
        print('4- Sair ')
        opcao = int(input('Opção: '))
        if opcao == 1:
            print(bin(n1)[2:])

        elif opcao == 2:
            print(oct(n1)[2:])

        elif opcao == 3:
            print(hex(n1)[2:])

        elif opcao == 4:
            print('Saindo... Até logo')
            break
        else:
            print('Digite uma opção válida! ')
            

    except ValueError:
        print('Digite um número válido! ')
            

