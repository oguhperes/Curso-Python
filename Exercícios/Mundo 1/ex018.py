# Ler se cidade começa com Santo ou não


try:
    print('\nSua cidade começa com santo? ')
    cidade = input('Cidade: ').lower().split()
    if 'santo' in cidade[0]:
       print('Sua cidade começa com santo! ')
    else:
       print('Sua cidade não começa com santo! ')

except ValueError:
    print('Digite um nome válido! ')
