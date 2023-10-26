print('Bem Vindo ao Atacado Hudson Cleiton de Paula')
valor_produto = float(input('Entre com o valor desejado: '))
qtd_produto = int(input('Entre com a quantidade desejada: '))
#apresentação e inserção de valores da compra

desconto_produto = 0
if qtd_produto <= 999:
  desconto_produto = 0.00
elif (1000 <= qtd_produto < 3000):
  desconto_produto = 0.03 # desconto de 3%
elif (3000 <= qtd_produto < 5000):
  desconto_produto = 0.05 # desconto de 5%
else:
  desconto_produto = 0.08 # desconto de 8%
#todos descontos aplicados

total_sem_desconto = valor_produto * qtd_produto
print('O valor total SEM deconto é de: R$ {:.2f}'.format(total_sem_desconto))
total_com_desconto = total_sem_desconto - total_sem_desconto * desconto_produto
print('O valor total COM deconto é de: R$ {:.2f}'.format(total_com_desconto))
#calculos das compras sem deconto e com desconto

print('Desconto de: {} %'.format(desconto_produto))
#informa o desconto recebido na compra
