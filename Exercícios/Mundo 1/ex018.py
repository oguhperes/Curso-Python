# Ler se cidade começa com Santo ou não


try:
    print('Sua cidade começa com "Santo"?\n ')
    cidade = input('Sua cidade: ').lower().split()
    if 'santo' in cidade[0]:
        print('Sua cidade começa com Santo! ')

    else:
        print('Sua cidade não começa com Santo! ')

except ValueError:
    print('Digite um nome válido! ')
