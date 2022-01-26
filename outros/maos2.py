from random import choice

modo = input('Qual modo voce quer jogar? ').split('v')

estado = [[1,1],[1,1]]
[[a1,a2],[b1,b2]] = estado

def jogada_ataque(jogador,mao_usada,mao_atacada):
    estado[1-jogador][mao_atacada] = (estado[1-jogador][mao_atacada] + estado[jogador][mao_usada]) % 5

def jogada_divisao(jogador):
    novo_valor = int(max(estado[jogador])/2)
    estado[jogador][0] = novo_valor
    estado[jogador][1] = novo_valor

def robo_joga(jogador):
    opcoes = ['jogada_ataque']
    if min(estado[jogador]) == 0 and max(estado[jogador]) % 2 == 0:
        opcoes.append('jogada_divisao')
    oque_fazer = choice(opcoes)
    if oque_fazer == 'jogada_ataque':
        mao_usada,mao_atacada = choice([0,1]),choice([0,1])
        while estado[jogador][mao_usada] == 0 or estado[1-jogador][mao_atacada] == 0:
            mao_usada,mao_atacada = choice([0,1]),choice([0,1])
        jogada_ataque(jogador,mao_usada,mao_atacada)
    else:
        jogada_divisao(jogador)

def humano_joga(jogador):
    if min(estado[jogador]) == 0 and max(estado[jogador]) % 2 == 0:
        oque_fazer = input('\natacar ou dividir? ')
    else:
        oque_fazer = 'atacar'
    if oque_fazer == 'atacar':
        mao_usada = int(input(f'\natacar com a mao 1[{estado[jogador][0]}] ou com a mao 2[{estado[jogador][1]}]? ')) - 1
        mao_atacada = int(input(f'atacar a mao 1[{estado[jogador-1][0]}] ou com a mao 2[{estado[jogador-1][1]}]? ')) - 1
        jogada_ataque(jogador,mao_usada,mao_atacada)
    else:
        jogada_divisao(jogador)

jogador = 0
rodada = 0
while estado[0] != [0,0] and estado[1] != [0,0]:
    print(f'\nRodada {rodada}\n{a1}\t{a2}\n\n\n\n{b1}\t{b2}')
    if modo[jogador] == 'P':
        humano_joga(jogador)
    else:
        robo_joga(jogador)
    [[a1,a2],[b1,b2]] = estado  
    jogador = 1 - jogador
    rodada += 1
print(f'\nRodada {rodada}\n{a1}\t{a2}\n\n\n\n{b1}\t{b2}')

if estado[0] == [0,0]: print('\nO jogador 2 ganhou o jogo!')
else: print('\nO jogador 1 ganhou o jogo!')
#exec(open('maos2.py').read())