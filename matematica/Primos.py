def primos(quantidade):
    primos = []
    for i in range(2,1000000000000000000):
        if len(primos) == quantidade: break
        n = 0
        for l in primos:
            if i % l == 0:
                n = 1
                break
        if n == 0:
            primos.append(i)
    return(primos)

def primos2(ponto_final):
    primos = []
    for i in range(2,ponto_final+1):
        n = 0
        for l in primos:
            if i % l == 0:
                n = 1
                break
        if n == 0:
            primos.append(i)
    return(primos)

print(primos2(500))
#exec(open('Primos.py').read())