from random import randint
estado = [[1,1],[1,1]]
[[a1,a2],[b1,b2]] = estado

def jogada(atacante,mao_usada,mao_atacada):
    estado[1-atacante][mao_atacada] = (estado[1-atacante][mao_atacada] + estado[atacante][mao_usada]) % 5
    [[a1,a2],[b1,b2]] = estado
    print(f'\nRodada {rodada}')
    print(f'{a1}\t{a2}\n\n\n{b1}\t{b2}')

def jogada_divisao(jogador):
    mao_dividida = max(estado[jogador][0],estado[jogador][1])
    estado[jogador][0] = int(mao_dividida/2)
    estado[jogador][1] = int(mao_dividida/2)
    [[a1,a2],[b1,b2]] = estado
    print(f'\nRodada {rodada}')
    print(f'{a1}\t{a2}\n\n\n{b1}\t{b2}')

def robo_joga(atacante):
    random = randint(0,1)
    if random == 0:
        if (estado[atacante][0] == 0 or estado[atacante][1] == 0) and max(estado[atacante][0],estado[atacante][1]) % 2 == 0:
            jogada_divisao(atacante)
        else:
            robo_joga(atacante)
    else:
        mao_usada = randint(0,1)
        mao_atacada = randint(0,1)
        if estado[atacante][mao_usada] == 0 or estado[1-atacante][mao_atacada] == 0:
            robo_joga(atacante)
        jogada(atacante,mao_usada,mao_atacada)

atacante = 0
rodada = 0
print(f'Rodada {rodada}')
print(f'{a1}\t{a2}\n\n\n\n{b1}\t{b2}')
while a1 != 0 and a2 != 0 or b1 != 0 and b2 != 0:
    rodada += 1
    robo_joga(atacante)
    atacante = 1 - atacante

print(f'\nO ganhador foi o jogador {atacante}')
#exec(open('maos.py').read())