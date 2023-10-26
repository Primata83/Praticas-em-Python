# PERGUNTA: Escreva um programa que calcule o preço a pagar pelo fornecimento de energia eletrica.
#pergunte a quantidade de kwh consumida e o tipo de instalação:
#R para residencias
#I para industrias
#C para comercio

kwh = float(input('Quantos kws?'))
tipo = input('Qual o tipo de instalação(R, C ou I)')

if (tipo == 'R'):
    if kwh <= 500:
        preco = 0.4
    else:
        preco = 0.65
elif (tipo == 'C'):
    if kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.6
elif (tipo == 'I'):
    if kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.6
else:
    print('Instalação invalida!')

print('Total a pagar: {}'.format(kwh * preco))

