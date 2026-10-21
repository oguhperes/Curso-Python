# Criar um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão.
# de zero até 20.
# O programa deverá ler um número pelo teclado (entre 0 e 20)
# E mostrar ele por extenso

lista = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
         'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    escolha = int(input('Digite um número entre (0 e 20): '))
    if escolha < 0 or escolha > 20:
        continue
    else:
        print(f'\nO número {escolha} por extenso é: {lista[escolha].capitalize()}')
        break
