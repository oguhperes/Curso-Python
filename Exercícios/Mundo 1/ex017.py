# Decomposição numeral


while True:
  try:
    n1 = int(input('Digite um número entre 0 e 9999: '))

    if n1 > 9999:
      print('Digite um número válido! ')

    else:
      n = str(n1)
      n = n.zfill(4)
      print(f'Milhar: {n[0]}')
      print(f'Centena: {n[1]}')
      print(f'Dezena: {n[2]}')
      print(f'Unidade: {n[3]}')
      
      
  except ValueError:
    print('Digite um número válido! ')


