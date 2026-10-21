# Criar uma tupla com os 20 primeiros coloados da Tabela do Campeonato Brasileiro de Futebol 
# na ordem de colocação. Depois mostre:
# Apenas os primeiros 5 colocados
# Os últimos 4 colocados
# Em ordem alfabética
# Em que posição na tabela está o time Chapecoense

clubs_list = ('Flamengo', 'Palmeiras', 'Athletico-PR', 'Fluminense', 'Bahia', 'Cruzeiro',
              'Atlético-MG', 'Santos', 'Bragantino', 'São Paulo', 'Coritiba', 'Vitória', 'Botafogo',
              'Vasco', 'Mirassol', 'Corinthians', 'Internacional', 'Grêmio', 'Remo', 'Chapecoense')
print('=' * 160)
print('\033[34mClubes do Brasileirão série A\033[0m ')
print(clubs_list)
print('=' * 160)
print('\033[34m5 primeiros times da liga\033[0m ')
print(clubs_list[:5])
print('=' * 160)
print('\033[34mÚltimos 4 times da liga\033[0m ')
print(clubs_list[16:])
print('=' * 160)
print('\033[34mClubes em ordem alfabética\033[0m ')
print(sorted(clubs_list))
print('=' * 160)
print('\033[34mPosição do Chapecoense na Tabela\033[0m ')
print(f'O time chapecoense está na posição número {clubs_list.index("Chapecoense")+1}')
print('=' * 160)



