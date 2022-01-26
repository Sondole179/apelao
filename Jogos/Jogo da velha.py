from random import choice

while True:
    modo = ''
    for i in list(input('Que modo voce quer jogar?(RvR ou PvP ou PvR) ')):
            if i != ' ':
                modo += i
    try:
        ['RvR','PvP','PvR','RvP'].index(modo)
        break
    except:
        print("\n('PvP' para player x player, 'PvR' para player x robo, 'RvR' para robo x robo)")
if modo == 'RvR': jogadores = ['R','R']
if modo == 'PvP': jogadores = ['P','P']
if modo == 'PvR' or modo == 'RvP':
    resposta = input("\nVoce deseja ser o jogador 'o' ou 'x'? ")
    while resposta != 'o' and resposta != 'x':
        resposta = input("Voce deseja ser 'o' ou 'x'? ")
    if resposta == 'o': jogadores = ['P','R']
    else: jogadores = ['R','P']

estado = ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]']
a1,a2,a3,b1,b2,b3,c1,c2,c3 = estado
espacos_vazios = [0,1,2,3,4,5,6,7,8]

def robo_joga(jogador):
    print(f'\n\nrodada {rodada}')
    x = choice(espacos_vazios)
    estado[x] = [' o ',' x '][jogador]
    espacos_vazios.remove(x)
    a1,a2,a3,b1,b2,b3,c1,c2,c3 = estado
    print(f'{a1}  {a2}  {a3}\n\n{b1}  {b2}  {b3}\n\n{c1}  {c2}  {c3}\n')

def humano_joga(jogador):
    estado_humano = estado[:]
    opcoes = []
    for i in range(9):
        if estado_humano[i] == '[ ]':
            opcoes.append(['a1','a2','a3','b1','b2','b3','c1','c2','c3'][i])
            estado_humano[i] = ['a1 ','a2 ','a3 ','b1 ','b2 ','b3 ','c1 ','c2 ','c3 '][i]
    d1,d2,d3,e1,e2,e3,f1,f2,f3 = estado_humano
    while True:
        print(f'\n{d1}  {d2}  {d3}\n\n{e1}  {e2}  {e3}\n\n{f1}  {f2}  {f3}')
        resposta = ''
        for i in list(input('\nEscolha uma das opcoes: ')):
            if i != ' ':
                resposta += i
        try:
            opcoes.index(resposta)
            break
        except:
            print(f'\n(as opcoes sao {opcoes})')
    espacos_vazios.remove(['a1','a2','a3','b1','b2','b3','c1','c2','c3'].index(resposta))
    estado[['a1','a2','a3','b1','b2','b3','c1','c2','c3'].index(resposta)] = [' o ',' x '][jogador]
    a1,a2,a3,b1,b2,b3,c1,c2,c3 = estado
    print(f'\n\nrodada {rodada}')
    print(f'{a1}  {a2}  {a3}\n\n{b1}  {b2}  {b3}\n\n{c1}  {c2}  {c3}\n')

jogador = 0
rodada = 0
while True:
    rodada += 1
    if jogadores[jogador] == 'P':
        humano_joga(jogador)
    else:
        robo_joga(jogador)
    a1,a2,a3,b1,b2,b3,c1,c2,c3 = estado
    jogador = 1 - jogador
    if any([a1==a2==a3!='[ ]',b1==b2==b3!='[ ]',c1==c2==c3!='[ ]',a1==b1==c1!='[ ]',a2==b2==c2!='[ ]',a3==b3==c3!='[ ]',a1==b2==c3!='[ ]',a3==b2==c1!='[ ]']) == True:
        print(f"\nO jogador '{['x','o'][jogador]}' ganhou o jogo!")
        break
    elif len(espacos_vazios) == 0:
        print('\nO jogo acabou empatado!')
        break

#exec(open('jogo da velha.py').read())