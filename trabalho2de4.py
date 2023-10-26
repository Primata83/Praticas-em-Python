print('Bem vindo A Loja de Açai e Cupuaçu do Hudson Cleiton de Paula')
print('--------------------CARDAPIO----------------------')
print('------| Tamanho | Cupuaçu (CP) | Açai (AC) |------')
print('------|    P    |   R$ 10,00   |  R$ 12,00 |------')
print('------|    M    |   R$ 15,00   |  R$ 17,00 |------')
print('------|    G    |   R$ 19,00   |  R$ 21,00 |------')
# tabela do cardapio da loja acima

acumulador = 0 

while True:
  sabor = input('Entre com o sabor do Açai ou Cupuaçu desejado: (CP|AC)') # escolha entre cupuaçu(CP) ou açai(AC)
  sabor = sabor.upper() # .upper faz com que o programa aceite letras maiusculas ou minusculas
  
  if sabor != 'CP' and sabor != 'AC':
    print('Sabor Invalido. Tente novamente')
    continue  # bloco pede o sabor do ac/cp ou mostra mensagem de erro se digitar as letras erradas
   
  tamanho = input('Entre com o tamanho do Açai ou Cupuaçu desejado: (P|M|G)')
  tamanho = tamanho.upper() # .upper faz com que o programa aceite letras maiusculas ou minusculas
  if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':# escolha o tamanho do cupuaçu ou açai
    print('Tamanho invalido. Tente novamente')
    continue # bloco pede tamanho p/m/g, mostra mensagem de erro e continua
  
  if sabor == 'CP' and tamanho == 'P':
    print('Você escolheu o Cupuaçu tamanho: P ')
    acumulador = acumulador + 10.00 # somando os valores
  
  elif sabor == 'CP' and tamanho == 'M':
    print('Você escolheu o Cupuaçu tamanho: M ')
    acumulador = acumulador + 15.00 # somando os valores

  elif sabor == 'CP' and tamanho == 'G':
    print('Você escolheu o Cupuaçu tamanho: G ')
    acumulador = acumulador + 19.00 # somando os valores

  elif sabor == 'AC' and tamanho == 'P':
    print('Você escolheu o Açai tamanho: P ')
    acumulador = acumulador + 12.00 # somando os valores
  
  elif sabor == 'AC' and tamanho == 'M':
    print('Você escolheu o Açai tamanho: M ')
    acumulador = acumulador + 17.00 # somando os valores

  elif sabor == 'AC' and tamanho == 'G':
    print('Você escolheu o Açai tamanho: G ')
    acumulador = acumulador + 21.00 # somando os valores
  
  pedir_mais = input('Deseja pedir mais alguma coisa? (S|N)') # escolha se quer pedir mais não
  pedir_mais = pedir_mais.upper() # .upper faz com que o programa aceite letras maiusculas ou minusculas
  if pedir_mais == 'S': # se escolher 'S' o programa continua
    continue
  else:
    print('O valor total a ser pago é de: R${:.2f}' .format(acumulador))
    break # termina o pedido e mostra o total somado
  
  print(acumulador) # soma os pedidos

  

