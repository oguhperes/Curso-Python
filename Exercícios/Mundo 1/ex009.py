
# Preço com desconto

try:
    preco = float(input('Preço do produto: R$ '))
    desc = preco * 0.05
    valor = preco - desc

    print(f'Com 5% de desconto fica R$ {valor:.2f}')

except ValueError:
    print('Digite um número válido! ')