while True: #decide a largura do retangulo
    try:
        largura = int(input("qual e a largura do retangulo? "))
        break
    except:
        print('vagabundo!')
        print('favor graziela digitar um numero valido')
while True: #decide a altura do retangulo
    try:
        altura = int(input("qual e a altura do retangulo? "))
        break
    except:
        print('vagabundo!')
        print('favor graziela digitar um numero valido')

retangulo = [largura,altura]
print(retangulo)

i = 0
while retangulo != [0,0]:
    if largura > altura:
        largura = largura - altura
        retangulo = [largura,altura]
        print(retangulo)
        i = i + 1
    else:
        altura = altura - largura
        retangulo = [largura,altura]
        print(retangulo)
        i = i + 1

print(f"\nforam necessario {i} quadrados")
#exec(open("quadrado.py").read())