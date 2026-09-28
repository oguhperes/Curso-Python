# Ler o nome e o preço de vários produtos
# Perguntar se o usuário vai continuar cadastrando, No final mostrar:
# Qual é o total gasto
# Quantos produtos custam mais de R$ 1000
# Qual é o nome do produto mais barato

mais_de_mil = 0
total_gasto = 0
valor_mais_barato = 99999999999999999999999999999999999
nome_mais_barato = ''
while True:
    print('\n=============================')
    print(' --- Caixa Supermercado --- ')
    print('=============================')
    nome_produto = input('Nome do produto: ')
    valor_produto = float(input('Preço: '))
    total_gasto += valor_produto
    if valor_produto >= 1000:
        mais_de_mil += 1
    if valor_produto < valor_mais_barato:
        valor_mais_barato = valor_produto
        nome_mais_barato = nome_produto
    resp = input('Quer continuar cadastrando? [S/N] ').lower().strip()
    while resp not in 'sn':
        resp = input('Quer continuar cadastrando? [S/N] ').lower().strip()
    if resp == 's':
        continue
    else:
        print(f'\nO total gasto foi: {total_gasto} ')
        print(f'{mais_de_mil} produtos custam mais de R$ 1000.00 ')
        print(f'O nome do produto mais barato é {nome_mais_barato} ')
        break