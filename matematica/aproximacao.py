from decimal import *
niveis = 1500 

getcontext().prec = int(niveis*1.5)
numero = Decimal(7)**Decimal(0.5)
numero_salvo = numero

x = numero - int(numero)
xs = []
for l in range(niveis):
    xs = [int(1/x)] + xs
    x = 1/x - int(1/x)

if niveis > 0:
    numerador = 1
    denominador = xs[0]
    for i in range(len(xs)-1):
        denominador_salvo = denominador
        denominador = numerador + xs[i+1] * denominador
        numerador = denominador_salvo
    numerador = int(numero) * denominador + numerador
    print(f"A aproximacao de {numero_salvo} e {numerador}/{denominador}")
else:
    print(f"Sua aproximacao e {int(numero)}")

#exec(open('aproximacao.py').read())