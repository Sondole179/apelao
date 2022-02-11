for a in range(2,10):
    for b in range(1,a):
        c,d = a**2 - b**2, 2*a*b
        print(c,d,int((c**2+d**2)**0.5))

#exec(open('triangulo.py').read()) 