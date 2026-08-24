# Empréstimo bancario, perguntar valor da casa, o salário do comprador e em quantos anos ele quer pagar
# se o valor da parcela for maior que 30% do salário não será possivel realizar o empréstimo

while True:
    try:
        print('\n--- Simulado empréstimo --- ')
        valor_da_casa = float(input('Valor da casa: '))
        salario = float(input('Seu salário: '))
        anos_desejados = int(input('Em quantos anos pretende pagar? '))
        verificacao_salario = salario * 0.3
        meses_da_parcela = anos_desejados * 12
        parcelas = valor_da_casa / meses_da_parcela

        if  parcelas > verificacao_salario:
                print('Empréstimo negado! Seu salário é muito baixo para realizar nessa quantidade de tempo')
                
        else:
            print(f'Empréstimo aprovado! Valor do empréstimo R$ {valor_da_casa} para pagar em {meses_da_parcela} parcelas de {parcelas:.2f}')
            break
    except ValueError:
        print('Error')

        

