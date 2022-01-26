name = input("say your name: ")

dificuldade = {
    'easy': 10,
    'normal': 50,
    'diff': 100
}

def jogo(primeiraVez):
    if primeiraVez:
        print(f"oi {name}! Quer brincar de adivinhação?")
    else:
        print(f"Foi divertido {name}! Quer brincar de novo?")

    res = ""
    while res != "yes" and res != "no":
        res = input("yes/no: ")

    if res == "no":
        print(f"adeus, até mais {name}")
        exit()

    print('Que bom! Quer jogar em qual nível?')

    nivel = input(' ou '.join(dificuldade.keys())+': ')
    
    print(f'Pensei num número entre 1 e {dificuldade[nivel]}. Sabe qual é?')

    import random
    N = random.randint(1,dificuldade[nivel])

    import math
    tentativas = int(math.ceil(math.log2(dificuldade[nivel])))

    print(f'voce tem {tentativas} tentativas.')

    acertou = False
    num_ten = 0
    while not acertou:
        guess = int(input('Escolha um numero: '))
        num_ten += 1
        if guess < N:
            print(f'{guess} é menor que o número que pensei!')
        elif guess > N:   
            print(f'{guess} é maior que o número que pensei!')
        else:
            print('Você acertou')
            acertou = True
        if num_ten == tentativas:
            print(f'Suas tentativas acabaram {name}!\n O numero que pensei é {N}.\n Melhor sorte na próxima =D')


    print('o jogo acabou!')
    jogo(primeiraVez=False)

jogo(primeiraVez=True)