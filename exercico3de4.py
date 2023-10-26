#funcão escolha o serviço abaixo
def escolha_servico():
  print('--------------------|Escolha o Serviço|--------------------')
  while True:
    servico = input('Qual serviço você deseja? \n' +
                  'a - DIG - Digitalização Digitalização \n' +
                  'b - ICO - Impressão Colorida \n' +
                  'c - IBO - Impressão Preto e Branco \n'+
                  'd - FOT - Serviço de Fotocópia \n' +
                  '>>')
    servico = servico.lower()
    servico = servico.strip()

    if servico == 'dig':
      return 1.10
    elif servico  == 'ico':
      return 1.00
    elif servico == 'ibo':
      return 0.40
    elif servico == 'fot':
      return 0.20
    else:
      print('Digite uma das opções dig/ico/ibo/fot')
      continue # voltar para o inicio (retorna para pergunta)

#função numero de paginas abaixo
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

#função serviço extra (adicional)
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
  

print('-----|Bem vindo a Copiadora do Hudson Cleiton de Paula|-----')
servicos = escolha_servico()
paginas = num_pagina()
extra = servico_extra()
total = (servicos * paginas) + extra
print('O Total Ficou em: R$ {:.2f} (Serviços: R$ {:.2f} * Paginas: R$ {:.2f}, Extra: R$ {:.2f})' .format(total,servicos,paginas,total))
