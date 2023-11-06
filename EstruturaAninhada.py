# TABUADA USANDO ESTRUTURA ANINHADA (while)
"""
tabuada = 1
while tabuada <= 10:
    print ('TABUADA DO {}:'.format(tabuada))
    while i <= 10:
        print('{} x {} = '.format(tabuada, i, tabuada * i))
        i += 1
    tabuada += 1
"""

# TABUADA USANDO ESTRUTURA ANINHADA (for)
# Sempre que você souber do numero correto que se vá usar, use FOR
for tabuada in range(1, 11):
    print('TABUADA DO {}:'.format(tabuada))
    for i in range(1, 11):
        print('{} x {} = {}'.format(tabuada, i, tabuada * i))

