palavras_salvo = (input('Escreva as palavras que voce deseja colocar em ordem alfabetica: ')).split()
palavras = [list(i) for i in palavras_salvo]
for j in range(len(palavras)):
    for l in range(len(palavras[j])):
        palavras[j][l] = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z','0','1','2','3','4','5','6','7','8','9'].index(palavras[j][l])
# 'Ola meu nome e Giordanni' = [[28, 23, 1], [25, 9, 41], [27, 29, 25, 9], [9], [12, 17, 29, 35, 7, 1, 27, 27, 17]]
#testeee
alfabetizado = []
while len(palavras) != 1:
    passaram_pela_leva = range(len(palavras))
    n = -1
    while len(passaram_pela_leva) != 1:
        tamanho_das_palavras = [len(palavras[i]) for i in passaram_pela_leva]
        if any([i == n+2 for i in tamanho_das_palavras]):
            passaram_pela_leva = [passaram_pela_leva[tamanho_das_palavras.index(min(tamanho_das_palavras))]]
            break
        n += 1
        leva = [[palavras[t][n],t] for t in passaram_pela_leva]
        passaram_pela_leva = [f[1] for f in leva if f[0] == min([t[n] for t in palavras])]
    # leva apresenta enésima letra de cada palavra e a posição dessa palavra em [palavras]
    # passaram_pela_leva apresenta as posiçõees das palavras que passaram pela eliminação da leva
    # EXEMPLO: palavras = [[19,1],[5,29],[13,17],[5,8]] / leva = [[19,0],[5,1],[13,2][5,3]] / passaram_pela_leva = [1,3]
    alfabetizado.append(palavras_salvo[passaram_pela_leva[0]])
    palavras_salvo.remove(palavras_salvo[passaram_pela_leva[0]])
    palavras.remove(palavras[passaram_pela_leva[0]])
alfabetizado.append(palavras_salvo[0])

for i in alfabetizado:
    print(i)
#exec(open('alfabetizador.py').read())