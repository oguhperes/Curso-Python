
# Conversor de moeda 

print(' --- Conversor de Moeda --- ')

try:
    real = float(input('Digite o valor R$ '))
    dol = real / 3.27

    print(f'Com R$ {real} você consegue U$ {dol:.2f} ')

except ValueError:
    print('Digite um número válido! ')