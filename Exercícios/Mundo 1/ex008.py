
# Área e quantidade de tinta pra parede 

try:
    l = float(input('Largura: '))
    h = float(input('Altura: '))
    a = l * h
    t = a / 2

    print(f'A parede tem {a}m\u00b2, e será necessário {t:.1f}L de tinta para pinta-la')

except ValueError:
    print('Digite um número válido! ')