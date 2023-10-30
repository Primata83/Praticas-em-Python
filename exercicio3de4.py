#funcão escolha o serviço abaixo
def escolha_servico():
  print('--------------------|Escolha o Serviço|--------------------')
  while True:
    servico = input('Qual serviço você deseja? \n' + # exibição no terminal de como vai aparecer a primeira escolha
                  'a - DIG - Digitalização Digitalização \n' +
                  'b - ICO - Impressão Colorida \n' +
                  'c - IBO - Impressão Preto e Branco \n'+
                  'd - FOT - Serviço de Fotocópia \n' +
                  '>>')
    servico = servico.lower() # lower vai converter tudo para letra maiuscula
    servico = servico.strip() # usado para remover espaços em branco

    if servico == 'dig': # serviços oferecidos
      return 1.10 # preço deste serviço
    elif servico  == 'ico':
      return 1.00
    elif servico == 'ibo':
      return 0.40
    elif servico == 'fot':
      return 0.20
    else:
      print('Digite uma das opções dig/ico/ibo/fot')
      continue # voltar para o inicio (retorna para pergunta)
# fim da função. Linha 2 a 24

# inicio da função numero de paginas abaixo
def num_pagina():
  print('--------------------|Número de Páginas|--------------------')
  while True:
    try:# caso apareça o erro ValueError, o programa segue normalmente
      qtd_pagina = int(input('Digite a quantidade desejada: \n')) # \n pula a linha
      if ( qtd_pagina < 10):
        return qtd_pagina * 1.00 # descon te 0%
      elif (qtd_pagina >= 10) and (qtd_pagina < 100):
        return qtd_pagina * 0.90 # desconto de 10%
      elif (qtd_pagina >= 100) and (qtd_pagina < 1000):
        return qtd_pagina * 0.85 # desconto de 15%
      elif (qtd_pagina >= 1000) and (qtd_pagina < 10000):
        return qtd_pagina * 0.80  # desconto de 20%
      else:
        print('Não aceitamos este número de páginas')
        continue # retorna para pergunta
    except ValueError: # ValueError é por uma letra ou um numero não decimal
      print('Digitar valores inteiros')
# fim da função. Linha 27 a 44      

# inicio função, serviço extra (adicional)
def servico_extra():
  print('--------------------|Adicional|--------------------')
  acumulador = 0
  while True:
    adicional = input('Deseja algum serviço adicional? \n' + 
                      '1 - Encardenação Simples - 10.00 \n' +
                      '2 - Encardenação Capa Dura - 25.00 \n'
                      '0 - Não desejo mais nada \n' +
                      '>>')
    if adicional == '1':
      acumulador = acumulador + 10.00
      continue # volta para o inicio do while true
    elif adicional == '2':
      acumulador = acumulador + 25.00
      continue # volta para o inicio do while true
    elif adicional == '0':
      return  acumulador
      continue # volta para o inicio do while true
    else:
        print('Digite uma das opções 1/2/0')
# fim da função serviço extra da linha 47 a 66

# inicio do bloco de exibição no terminal
print('-----|Bem vindo a Copiadora do Hudson Cleiton de Paula|-----')
servicos = escolha_servico()
paginas = num_pagina()
extra = servico_extra()
total = (servicos * paginas) + extra # multiplicação e soma de tudo (:.2f formata um número em ponto flutuante com duas casas decimais)
print('O Total Ficou em: R$ {:.2f} (Serviços: R$ {:.2f} * Paginas: R$ {:.2f}, Extra: R$ {:.2f})' .format(total,servicos,paginas,extra))
# fim da função. Linha 69 a 74 chama as funções e exibe no console o total, serviço, paginas com ou sem desconto e o serviço extra