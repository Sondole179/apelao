from math import factorial as fac

palavra = list(input('Escolha uma palavra: '))
combinacoes = fac(len(palavra)) * ['']

for i in palavra:
    
#exec(open('nomes2.py').read())