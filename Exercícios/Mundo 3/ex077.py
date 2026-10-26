# Criar um programa onde deve-se digitar uma expressão matemática qualquer
# que use parênteses. O programa deve analisar se a expressão está com os 
# parênteses abertos ou fechados ex: (() errado (()) certo

cont_abrir = 0
cont_fechar = 0
lista = list()
quest = input('Digite a expressão com parênteses: ')
lista.append(quest)
for c in lista:
    if c == '(':
        cont_abrir += 1
    if c == ')':
        cont_fechar += 1
if cont_fechar != cont_abrir:
    print('Expressão inválida! ')
else:
    print('Expressão válida! ')
