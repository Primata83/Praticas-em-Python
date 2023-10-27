#------------------inicio da variaveis globais------------------
lista_livros = []
codigo_livro = 0
#-----------------fim das variaveis globais-----------------

#-----------------inicio de cadastrar produto-----------------
def cadastrar_livro(codigo):
  print('Bem vindo ao menu de Cadastrar Livro')
  print('Código do Produto {}'.format(codigo))
  id = input('Entre com o ID do Livro:')
  nome = input('Coloque o NOME do Livro:')
  autor = input('Nome do AUTOR do Livro:')
  editora = input('Nome da EDITORA do Livro:')
  id_global = {'id'      : id,
               'nome'    : nome,
               'autor'   : autor,
               'editora' : editora}
  lista_livros.append(id_global.copy())             
#-----------------fim de cadastrar produto-----------------

#-----------------inicio de Consultar Livro-----------------
def consultar_livro():
  print('Bem vindo ao menu de Consultar Livros')
  while True:
    opcao_consultar = input('\nEscolha a opção desejada: \n' +
                            '1 - Consultar TODOS Livros \n' +
                            '2 - Consultar Livros por CÓDIGO \n' +
                            '3 - Consultar por AUTOR \n' +
                            '4 - Retornar \n' +
                            '>>>')
    if opcao_consultar == '1': # num menu, sempre se usa if, elif e else
      print('Você escolheu a opção Todos os Livros')
      for livro in lista_livros: # livro vai varrer toda a lista de livros
        print('--------------------------')
        for key, value in livro.items(): # varrer todos os conjuntos chave e valor do dicionario produto
          print('{}:{}' .format(key,value)) # imprime chave e valor no terminal
        print('--------------------------')
    elif opcao_consultar == '2':
      print('Você escolheu a opção Livros por Código')
      codigo_desejado = int(input('Entre com o Código do Livro'))
      for livro in lista_livros:
        if livro['id'] == codigo_desejado: # o valor do campo codigo desse id_global e igual o valor desejado
          print('--------------------------')
          for key, value in livro.items(): # varrer todos os conjuntos chave e valor do dicionario produto
            print('{}:{}' .format(key,value)) # imprime chave e valor no terminal
        print('--------------------------') 
    elif opcao_consultar == '3':
      print('Você escolheu a opção Livro(s) por Autor')
      codigo_desejado = input('Escolha Livros por Autor')
      for livro in lista_livros:
        if livro['autor'] == codigo_desejado: # o valor do campo codigo desse id_global e igual o valor desejado
          print('--------------------------')
          for key, value in livro.items(): # varrer todos os conjuntos chave e valor do dicionario produto
            print('{}:{}' .format(key,value)) # imprime chave e valor no terminal
        print('--------------------------') 
    elif opcao_consultar == '4':
      return # sai da função contultar e volta para o menu
    else: # retorna para o inicio (da maneira mais comum)
      print('Opção invalida Tente Novamente') 
      continue # continue faz voltar para o inicio do laço (é uma segunda maneira disto acontecer)
#-----------------fim de Consultar Livros-----------------

#-----------------inicio de Remover Livro-----------------
def remover_livro():
  print('Digite o ID do Livro para ser Removido')
  codigo_desejado = input('Entre com o ID do produto que deseja remover: ')
  for livro in lista_livros:
    if livro['id'] == codigo_desejado:
      lista_livros.remove(livro)
      print('Livro Removido!')
#-----------------fim de Remover Livro-----------------

#-----------------INICIO DO MENU PRINCIPAL-----------------
print('---Bem Vindo ao Controle de Livros Hudson Cleiton de Paula---')
while True:
  opcao_principal = input('Escolha a opção desejada: \n' +
                          '1 - Cadastrar Livros \n' +
                          '2 - Consultar Livros \n' +
                          '3 - Remover Livros \n' +
                          '4 - Sair \n' +
                          '>>>')
  if opcao_principal == '1': # num menu, sempre se usa if, elif e else
    codigo_livro = codigo_livro + 1
    cadastrar_livro(codigo_livro)
  elif opcao_principal == '2':
    consultar_livro()
  elif opcao_principal == '3':
    remover_livro()
  elif opcao_principal == '4':
    break # encerra o laço principal e o programa acaba
  else:
    print('Opção invalida Tente Novamente') 
    continue # continue faz voltar para o inicio do laço (é uma segunda maneira disto acontecer)
##-----------------FIM DO MENU PRINCIPAL-----------------