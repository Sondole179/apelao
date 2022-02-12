from random import choice

estado = ['[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]','[ ]']
e1,e2,e3,e4,e5,e6,e7,e8,e9 = estado
posicoes_livres = [i for i in range(9)]

def robo_ataca(jogador):
    escolha = choice(posicoes_livres)
    estado[escolha] = jogador
    posicoes_livres.remove(escolha)

jogador = 1
rodada = 0
while 1 - any([len(posicoes_livres)==0,e1==e2==e3!='[ ]',e4==e5==e6!='[ ]',e7==e8==e9!='[ ]',e1==e4==e7!='[ ]',e2==e5==e8!='[ ]',e3==e6==e9!='[ ]',e3==e4==e7!='[ ]',e1==e5==e9!='[ ]']):
    jogador = 1 - jogador
    rodada += 1
    robo_ataca([' x ', ' o '][jogador])
    e1,e2,e3,e4,e5,e6,e7,e8,e9 = estado
    print(f'\nRodada {rodada}\n{e1} {e2} {e3}\n\n{e4} {e5} {e6}\n\n{e7} {e8} {e9}')

if any([e1==e2==e3!='[ ]',e4==e5==e6!='[ ]',e7==e8==e9!='[ ]',e1==e4==e7!='[ ]',e2==e5==e8!='[ ]',e3==e6==e9!='[ ]',e3==e5==e7!='[ ]',e1==e5==e9!='[ ]']):
    print(f"\nO jogador {[['x'],['o']][jogador]} ganhou o jogo!")
else:
    print('\nO jogo abacou dando velha!')
#exec(open('jogos/jogo_da_velha2.py').read())