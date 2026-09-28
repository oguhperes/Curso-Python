# Par ou ímpar. O jogo sera interrompido quando o jogador perder
# mostrando o total de vitórias consecutivas

from time import sleep
from random import randint
cont_vitoria = 0
while True:
    sleep(0.6)
    print('\n ==== Par ou ímpar ==== ')
    escolha_imp_par = input('Ímpar ou par [I/P]: ').lower()
    escolha_usuario_num = int(input('Digite um número entre 0 e 10: '))
    escolha_computador_num = randint(0, 10)
    soma = escolha_usuario_num + escolha_computador_num
    if (
        (escolha_imp_par == 'i' and soma % 2 != 0) or
        (escolha_imp_par == 'p' and soma % 2 == 0)
    ):
        print(f'Você ganhou!')
        print(f'Eu escolhi {escolha_computador_num} | {escolha_usuario_num} + {escolha_computador_num} = {soma} !!! ')
        cont_vitoria += 1
    else:
        print('==============================')
        print('Você perdeu! ')
        print(f'Eu escolhi {escolha_computador_num} | {escolha_usuario_num} + {escolha_computador_num} = {soma} !!! ')
        print(f'Você tinha uma sequência de {cont_vitoria} vitória(s)\n')
        break