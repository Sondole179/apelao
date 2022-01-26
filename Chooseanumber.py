from random import choice

while True:
    dificuldade = input('Choose a difficulty mode: ')
    try:
        nivel = int(dificuldade)
        break
    except:
        if any([dificuldade=='do you hate your self?',dificuldade=='impossible',dificuldade=='very hard',dificuldade=='hard',dificuldade=='medium',dificuldade=='easy']):
            nivel = [1000000000,1000000,20000,1000,200,10][[dificuldade=='do you hate your self?',dificuldade=='impossible',dificuldade=='very hard',dificuldade=='hard',dificuldade=='medium',dificuldade=='easy'].index(True)]
            break
        print("\n(easy, medium, hard, very hard, impossible, do you hate your self? or just type a number for difficulty level)")
paia = input("do you want to play in 'cafe com leite' mode? ")
print("ok! let's play!")

numero = choice(range(nivel))
expoente = 0
while 2**expoente < nivel:
    expoente += 1
tentativas = expoente

if paia == 'no': print(f"\nThe number I choose is less than {nivel}")
else: print(f'\n-1 < n < {nivel}')
print(f'({tentativas+1} attempts left)')
resposta = int(input('Try a number: '))
min,max = -1,nivel
while resposta != numero and tentativas > 0:
    if paia == 'no':
        if resposta > numero: print(f'\nThe number i choose is less than {resposta}.')
        else: print(f'\nThe number i choose is greater than {resposta}.')
    else:
        if resposta > numero and min<resposta<max: max = resposta
        if resposta < numero and min<resposta<max: min = resposta
        print(f'\n{min} < n < {max}')
    print(f'({tentativas} attempts left)')
    tentativas -= 1
    resposta = int(input('Try a number: '))

if resposta == numero: print(f'\nCongratulations! You got the number I choose!')
else: print(f'\nNo more attempts left, the number i choose is {numero}')
#exec(open('Chooseanumber.py').read())