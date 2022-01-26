forma = input("escolha uma forma geométrica: ")

def redondo():
    escolha = print(input("deseja inserir raio ou diametro? "))
    if escolha == "raio":
        raio = int(input("qual e o tamanho do raio? "))
        print(f"a area do circulo e {3.14*raio**2} e o seu perimetro e {6.28*raio}")
    if escolha == "diametro":
        diametro = int(input("qual e o tamanho do diametro? "))
        print(f"a area do circulo e {1.57*diametro**2} e o seu perimetro e {3.14*diametro}")
    else:
        redondo()

def rodada(forma):
    if forma == "quadrado":
        tamanho = int(input("qual e o tamanho do seu lado? "))
        print(f"a area do quadrado e {tamanho**2} e o seu perimetro e {tamanho*4}")
    if forma == "retangulo":
        x = int(input("qual e a largura? "))
        y = int(input("qual e o comprimento dele? "))
        print(f"a area do retângulo é {x*y} e o seu perimetro e {2*(x+y)}")
    if forma == "circulo":
        redondo() 
    if forma == "paralelepipedo":
        x = int(input("qual e a largura do paralelepipedo? "))
        y = int(input("qual e o comprimento do paralelepipedo? "))
        z = int(input("qual e a altura do paralelepipedo? "))
        print(f"\nparelelepipedo{x,y,z}\nvolume: {x*y*z}\nperimetro: {2*(x*y+x*z+y*z)}")
    else:
        forma = input("escolha uma forma geométrica válida: ")
        rodada(forma)

rodada(forma)

#python geometria.py