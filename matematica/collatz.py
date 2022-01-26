def collatz(numero):
    collatz = [numero]
    while numero != 1 and numero != -1:
        if numero % 2 == 0: 
            numero = int(numero/2)
        else: 
            if numero > 0: numero = numero*3 + 1
            else: numero = numero*3 - 1
        collatz.append(numero)
    return(collatz)

def collatz_legivel():
    while True:
        numero = input('Que numero vai iniciar a? ')
        try: 
            int(numero) == float(numero)
            numero = int(numero)
            break
        except:
            print('\nDigite um numero inteiro')
    a = collatz(numero)
    for i in a:
        print(i)
    if numero != 1 and numero != -1: print(f'\nO numero {numero} teve {len(a)} sucessores de collatz!!')
    else: print(f'\nO numero {numero} teve 1 sucessor de collatz!!')
    if numero > 0: print(f'Chegou a um pico de {max(a)}.')
    else: print(f'Chegou a um pico de {min(a)}.')

def pescando_grande(aqui,ate_aqui):
    for i in range(aqui,ate_aqui):
        print(f'{i}\t{len(collatz(i))}')
#cheguei a conclusão que o número mais apelão de collatz é 27

collatz_legivel()
#exec(open("collatz.py").read())