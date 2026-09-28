# Decomposição numeral


while True:
  try:
    numero = int(input('\nDigite o número entre 1 e 9999: '))
    if numero < 1 or numero > 9999:
      print('Digite um número válido! ')
    else:
      numero = str(numero)
      numero = numero.zfill(4)
      print(f'Milhar: {numero[0]}')
      print(f'Centena: {numero[1]}')
      print(f'Dezena: {numero[2]}')
      print(f'Unidade: {numero[3]}')
      break
      
  except ValueError:
    print('Digite um número válido! ')


