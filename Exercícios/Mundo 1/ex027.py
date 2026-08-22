# Ler 3 números e mostrar qual é maior e menor

try:
   n1 = float(input('Primeiro número: '))
   n2 = float(input('Segundo número: '))
   n3 = float(input('Terceiro número: '))
   maximo = max(n1, n2, n3)
   minimo = min(n1, n2,n3)
   print(f'O maior número é {maximo} e o menor número é {minimo}')

except ValueError:
    print('Digite um número válido! ')
