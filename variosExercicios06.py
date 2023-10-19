# >>> Booleanos <<<

# PERGUNTA: 2 + 2 é igual a 4 ?
#print(2 + 2 < 4)

# PERGUNTA: O valor 7//3 é igual a 1 + 1?
#print(7 // 3 == 1 + 1)

# PERGUNTA: A soma de 3 elevado ao quadrado com 4 elevado ao quadrado é igual a 25?
#ao quadrado é sempre 2
#print(3**2 + 4**2 == 25)

# PERGUNTA: A soma de 2, 4 e 6 é maior que 12
#print(2 + 4 + 6 > 12)

# PERGUNTA: 1387 é divisivel por 19?
"""
n1 = 1387
n2 = 19
divisao = (n1 % n2 == 0)
print(divisao)
"""

# PERGUNTA: 31 é par
#é necessário usar : no final da linha que inicia um bloco de código após a estrutura if, else, elif,
#loops for e while, definições de funções, classes, e assim por diante. O : é usado para indicar o
#início de um bloco de código e é uma parte fundamental da sintaxe do Python.
"""
n1 = 31
if n1 % 2 == 0:
    print('é par')
else:
    print('é impar')
"""

# PERGUNTA: O menor valor entre: 34, 29, e 31 é menor do que 30?
#elif é a palavra chave em python usada para ter  tres condições ou mais.
#elif é sempre usado entre o if e else
"""
valor1 = 34
valor2 = 29
valor3 = 31

if valor1 < valor2 and valor1 < valor3:
    menor_valor = valor1
elif valor2 < valor3:
    menor_valor = valor2
else:
    menor_valor = valor3

print(f"O menor valor entre {valor1}, {valor2} e {valor3} é: {menor_valor}")
"""

