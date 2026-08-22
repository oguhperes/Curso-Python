
# Converter metros para centimetros e milimetros

try:
    m = float(input('Metros: '))
    c = m * 100
    mm = m * 1000

    print(f'{m} metros são {c:.2f} centímetros e {mm:.2f} milímetros ')

except ValueError:
    print('Digite um número váido! ')