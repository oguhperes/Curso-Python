# Ler ano de nascimento de uma pessoa e informar conforma a idade:
# Se ele vai se alistar futuramente, se é a hora de se alistar, se ja passou do tempo de se alistar, mostrar também o tempo
# que falta ou passou do prazo

try:
    print(' --- Consultar seu status de serviço militar --- ')
    ano = int(input('Em que ano você nasceu? '))
    idade = 2026 - ano
    

except ValueError:
    print('Digite um número válido! ')