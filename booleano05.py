#conta = 31
#porcen = (31 % 10)
#print(porcen)

conta = 31
porcen = (conta % 24)

if porcen == 1:
    print("O resto é 1")
elif porcen == 0:
    print("O resto é 0")
else:
    print("O resto é diferente de 0 e 1")
