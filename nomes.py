from math import factorial as fac

palavra = list(input('Escreva uma palavra: '))
combinacoes = fac(len(palavra)) * ['']

for i in range(len(palavra)):
    for l in range(fac(i+1)):
        combinacoes[l] += f'{palavra[i]}'
        for t in range(len(combinacoes[l])):
            combinacoes += combinacoes.index(t)

for i in combinacoes:
    print(i)

#exec(open('nomes.py').read())