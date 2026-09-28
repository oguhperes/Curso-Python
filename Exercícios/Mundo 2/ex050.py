# Ler nome, idade e sexo de 4 pessoas. No final do programa mostre:
# A média de idade do grupo
# Qual nome do homem mais velho
# Quantas mulheres tem menos de 20 anos

try:
    soma_idades = 0
    mulheres_menos_vinte = 0
    i1 = 0
    nome_mais_velho = ''
    for i in range(1, 5):
        print(f' ----- {i}ª PESSOA ----- ')
        nome = input('Nome: ').capitalize()
        idade = int(input('Idade: '))
        sexo = input('Sexo [M/F]: ').lower().strip()
        soma_idades += idade
        if sexo == 'm':
            if idade > i1:
                i1 = idade  
                nome_mais_velho = nome
        if sexo == 'f':
            if idade < 20:
                mulheres_menos_vinte += 1    
    media = soma_idades /4
    print(f'A média é {media}, o nome do mais velho é {nome_mais_velho}, tem {mulheres_menos_vinte} mulheres com menos de 20')
except ValueError:
    print('Digite um número válido! ')
    
