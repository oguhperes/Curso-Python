# Criar um programa que contenha uma única tupla com nomes de produtos
# e seus respectivos preços
# No final mostre uma listagem de preços, organizando-os em forma tabular

print('-' * 50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-' * 50)
products = ('Pão', 12.99, 'Leite', 4.50,'Manteiga', 12.99, 'Achocolatado', 9.99, 'Arroz', 24.99, 'Suco de Uva', 11.99,
            'Farinha', 9.99, 'Banana', 8, 'Feijão', 12.99, 'Energético', 9.99, 'Leite em Pó', 7.99)
for pos in range(0, len(products)):
    if pos % 2 == 0:
        print(f'{products[pos]:.<39}', end='')
    else:
        print(f'R${products[pos]:>8.2f}')
print('-' * 50)
