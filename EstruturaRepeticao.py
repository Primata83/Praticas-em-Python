"""
EXERCICIO: while (contador)

x = 1
while(x <= 99):
    print('numero {}'.format(x))
    x = x + 1
"""


#EXERCICIO: while > Pegando os numeros pares de 5 a 10

inicial = int(input('digite o um numero inicial:'))# a palavra ``input`` pede para o usuario colocar uma entrada do usuario pelo console e SEMPRE sera uma string
final = int(input('digite o final:'))# a palavra ``input`` pede para o usuario colocar uma entrada do usuario pelo console e SEMPRE sera uma string
print('-----------------------')
print('Os numeros pares são os:')

x = inicial # variavel 
while (x <= final): #---- passando para o programa q o loop só vai até a variavel final(= 10) 
    if (x % 2 == 0): #--- verificando se é par ou não (sendo x = inicial, usando %)
        print(x) # ------ saida
    x = x + 1 # --------- incremento
    