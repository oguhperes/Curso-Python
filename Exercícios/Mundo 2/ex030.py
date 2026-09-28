# Empréstimo bancario, perguntar valor da casa, o salário do comprador e em quantos anos ele quer pagar
# se o valor da parcela for maior que 30% do salário não será possivel realizar o empréstimo

while True:
    try:
        print(' \n--- Empréstimo Bancário --- ')
        valor_da_casa = int(input('Valor da casa: '))
        salario = float(input('Salário: '))
        anos = int(input('Anos: '))
        verificacao_salarial = salario * 0.3
        valor_parcelas = (valor_da_casa / anos) / 12

        if valor_parcelas > verificacao_salarial:
            print(f'EMPRÉSTIMO NEGADO!!! Seu salário é muito baixo ')
        else:
            parcela = anos * 12
            print(f'EMPRÉSTIMO APROVADO!!! Com parcelas de R$ {valor_parcelas:.2f}, em {parcela} Meses')
        break
    except ValueError:
        print('Error')

    

