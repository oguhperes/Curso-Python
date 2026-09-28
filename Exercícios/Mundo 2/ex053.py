# Ler dois valores e mostrar um menu na tela: (usando while)
# 1 - somar
# 2 - multiplicar
# 3 - maior
# 4 - digitar novos números ()
# 5 - sair

while True:
    print('\n --- Calculadora --- ')
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    print('\nEscolha uma operação:')
    print('1 - Somar')
    print('2 - Multiplicar')
    print('3 - Maior número')
    print('4 - Digitar novos números')
    print('5 - Sair')
    opcao = int(input('Opção: '))

    if opcao == 1:
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}')
    elif opcao == 2:
        multiplicar = n1 * n2
        print(f'{n1} x {n2} = {multiplicar}')
    elif opcao == 3:
        maior = max(n1, n2)
        print(f'O maior número entre {n1} e {n2} é {maior}')
    elif opcao == 4:
        continue
    elif opcao == 5:
        break
    else:
        print('Digite um número válido! ')


if opcao == None:
    print('oi')