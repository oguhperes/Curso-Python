# Criar um programa que tenha uma tupla com várias palavras (não usar acento)
# Depois disso você deve mostrar para cada palavra quais são suas vogais

palavras = ('jiboia', 'bagre', 'gorjerta', 'santos', 'trabalhar', 'futuro', 'gratis', 'licenciamento',
            'futuro', 'cimento')
for c in palavras:
    print(f'Na palavra {c.upper()} temos', end=' ')
    for letra in c:
        if letra in 'aeiou':
            print(letra, end=' ')
    print()