lista = [2.7,0,5.788,1,1,3]
lista2 = [3,6,7,2,0,4,7,3,5]

def lista_polinomio(lista):
    polinomio = ""
    for i in range(len(lista)):
        if lista[i] != 0:
            if lista[i] != 1 or i == 0:
                polinomio += f"{lista[i]}"
            if i != 0:
                polinomio += "x"
                if i > 1:
                    polinomio += f"^{i}"
        if i < len(lista) - 1:
            if lista[i+1] > 0:
                polinomio += " + "
            if lista[i+1] < 0:
                lista[i+1] *= -1
                polinomio += " - "
    return(polinomio)

def soma_de_polinomios(lista,lista2):
    lista_resultado = []
    if len(lista) > len(lista2):
        lista2 += [0]*(len(lista)-len(lista2))
    else:
        lista += [0]*(len(lista2)-len(lista))
    for i in range(len(lista)):
        lista_resultado.append(lista[i]+lista2[i])
    return lista_resultado

def mutiplicacao_de_polinomios(a,b):
    lista = [0 for j in range(len(a)+len(b)-1)]
    for i in range(len(a)):
        for l in range(len(b)):
            lista[i+l] += a[i]*b[l]
    return lista

pol = [1]
for i in range(11):
    print(lista_polinomio(pol))
    pol = mutiplicacao_de_polinomios(pol,[1,1])

#exec(open("polinomios.py").read())