# PERGUNTA: Escreva um algoritmo que leia dos valores numericos e que pergunte ao usuario qual operação ele deseja
# realizar: adição (+), subtração (-) multiplicação (*) ou divisão (/). Exiba na tela o resultado da operação desejada
#(exercicio da apostila - aula 3)

print('CALCULADORA')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Pressione outra tecla para sair')

op = input('Qual operação deseja fazer?')
if op == '+' or op == '-' or op == '*' or op == '/':
    x = int(input('Digite o primeiro valor'))
    y = int(input('Digite o segundo valor'))

if (op == '+'):
    res = x + y
    print('Resultado: {} + {} = {}'.format(x, y, res))
elif (op == '-'):
    res = x - y
    print('Resultado: {} - {} = {}'.format(x, y, res))
elif (op == '*'):
    res = x * y
    print('Resultado: {} * {} = {}'.format(x, y, res))
elif (op == '/'):
    res = x / y
    print('Resultado: {} / {} = {}'.format(x, y, res))
else:
    print('Operação invalida.')

print('Encerrando o programa...')