while True:
    lista = (input("digite um ou mais numeros: ")).split()
    listasalva = []
    n = 0
    try:
        for i in range(len(lista)):
            lista[i] = int(lista[i])
            listasalva.append(lista)
            if lista[i] < 0:
                lista[i] *= -1
            if lista[i] == 0:
                n = 1
        break
    except:
        print("digite apenas numeros inteiros, separado por espacos")

def mdc(lista):
    for i in range(len(lista)):
        while lista[i] != lista[i+1]:
        return(lista)

mdc(lista) 
print(lista)



#exec(open("mdc.py").read())
#python mdc.py