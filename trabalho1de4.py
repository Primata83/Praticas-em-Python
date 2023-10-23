print('Bem Vindo a Loja do Hudson Cleiton de Paula')
valor_produto = float(input('Entre com o valor desejado: '))
qtd_produto = int(input('Entre com a quantidade desejada: '))
desconto_produto = 0
if qtd_produto <= 999:
  desconto_produto = 0.00
elif (1000 >= qtd_produto < 3000): 
  desconto_produto = 0.03 # desconto de 3% 
elif (3000 >= qtd_produto < 5000): 
  desconto_produto = 0.05 # desconto de 5% 
else:
  desconto_produto = 0.08 # desconto de 8%
print(desconto_produto)

