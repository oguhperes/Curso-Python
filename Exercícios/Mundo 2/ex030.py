# Empréstimo bancario, perguntar valor da casa, o salário do comprador e em quantos anos ele quer pagar
# se o valor da parcela for maior que 30% do salário não será possivel realizar o empréstimo

while True:
    try:
        # Perguntas como: Valor da casa, salário, e anos desejados para pagar
        print('\n--- Simulador de Empréstimo --- ')
        valor_da_casa = float(input('Valor da casa: '))
        salario = float(input('Salário: '))
        anos_planejados = int(input('Em quantos anos planeja pagar: '))
        # Verificações
        verificacao_salarial = salario * 0.3
        meses_emprestimo = anos_planejados * 12
        valor_parcelas = valor_da_casa / meses_emprestimo

        if valor_parcelas > verificacao_salarial:
            print('Empréstimo negado! Seu salário é muito baixo ')

        else:
            print(f'Empréstimo aprovado! Com parcelas de R$ {valor_parcelas:.2f} por {meses_emprestimo} meses  ')
            break
    except ValueError:
        print('Error')

    

