numero = []

for i in range(0,6):
    inserirnumero = int(input("digite um numero"))
    if inserirnumero % 3 ==0:
      numero.append(inserirnumero)

soma = sum(numero)
print(soma)