# Ler se tem silva no nome


try:
   print('\nTem silva no seu nome? ')
   nome = input('Seu nome: ').lower().split()
   if 'silva' in nome:
        print('Seu nome tem Silva! ')
   else:
       print('Seu nome não tem Silva! ')
   
except ValueError:
    print('Digite um nome válido! ')
