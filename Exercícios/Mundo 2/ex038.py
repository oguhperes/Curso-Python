# Calcular valores pagos em produtos
# À vista, dinheiro/cheque: 10% de desconto
# À vista no cartão 5% de desconto
# em até 2x no cartão, preço normal
# 3x ou mais 20% de juros

while True:
    try:
        print(' \n--- Caixa Supermercado --- ')
        valor = float(input('Valor do produto: '))
        if valor <= 0:
            print('Digite um valor válido! ')
            continue

        else:
            print('\nEscolha uma opção: ')
            print('1- Dinheiro/ Débito')
            print('2- Crédito ')
            opcao = int(input('Opção: '))

            if opcao == 1:
                a_vista = valor * 0.1
                valor -= a_vista
                print(f'Seu produto com desconto custa R$ {valor:.2f}')

            elif opcao == 2:
                parcelas = int(input('Parcelas: '))
                if parcelas <= 0:
                    print('Digite um número válido! ')
                    continue
                else:
                    if parcelas == 1:
                        parcelado = valor * 0.05
                        valor -= parcelado
                        print(f'Seu produto custará R$ {valor:.2f}')

                    elif parcelas == 2:
                        parcelas_quantidade = valor / 2
                        print(f'Seu produto custará R$ {valor:.2f}')
                        print(f'com 2 parcelas de R$ {parcelas_quantidade:.2f}')

                    else:
                        parcelado = valor * 0.2
                        valor += parcelado 
                        parcelas_quantidade = valor / parcelas
                        print(f'Seu produto custará R${valor:.2f}')
                        print(f'com {parcelas} parcelas de R$ {parcelas_quantidade:.2f}')
            
            else:
                print('Digite uma opção válida! ')
                continue
            break
    except ValueError:
        print('Digite um número válido! ')