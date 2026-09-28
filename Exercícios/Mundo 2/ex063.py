# Ler idade e sexo de várias pessoas. A cada pessoa cadastrada o programa deverá pergunta
# se o usuário quer ou não continuar. No final mostre:
# Quantas pessoas tem mais de 18 anos
# Quantos homens foram cadastrados
# Quantas mulheres tem menos de 20 anos

cont_homens = 0
cont_mulheres = 0
mais_dezoito = 0
while True:
    nome = input('\nDigite o nome: ')
    idade = int(input('Sua idade: '))
    sexo = input('Digite o sexo [F/M]: ').lower().strip()
    if sexo == 'm':
        cont_homens += 1
    if sexo == 'f' and idade < 20:
        cont_mulheres += 1
    if idade >= 18:
        mais_dezoito += 1
    resp = input('Quer continuar? [S/N] ').lower().strip()
    while resp not in 'ns':
        resp = input('Quer continuar? [S/N] ').lower().strip()
    if resp == 's':
        continue
    else:
        print(f'{mais_dezoito} pessoas tem mais de 18 ')
        print(f'{cont_mulheres} mulheres tem menos de 20 anos ')
        print(f'{cont_homens} homens foram cadastrados ')
        break


