from decimal import Decimal as dec
def fibonacci(quantidade):
    x,y = 0,1
    li = []
    while len(li) < quantidade-1:
        li.append(x)
        li.append(y)
        x += y
        y += x
    if quantidade % 2 == 1:
        li.append(x)
    return li
def reverse_fibonacci(quantidade):
    x,y = 0,1
    li = []
    while len(li) < quantidade-1:
        li.append(x)
        li.append(y)
        x -= y
        y -= x
    if quantidade % 2 == 1:
        li.append(x)
    return li

while True:
    quantidade = input('Quantos sucessores de fibonacci voce quer? ')
    try: 
        int(quantidade) == float(quantidade)
        quantidade = int(quantidade)
        break
    except:
        print('\nDigite um numero inteiro')

if quantidade < 0: 
    a = reverse_fibonacci(quantidade*-1)
else: 
    a = fibonacci(quantidade)

for i in a:
    print(i)
if quantidade != 1 and quantidade != -1: print(f'\nAssim como foi pedido, foram impressos {quantidade} sucessores de fibonacci!')
else: print(f'\nAssim como foi pedido, foi impresso {quantidade} sucessor de fibonacci!')
if len(a) > 2:
    print(f"a melhor aproximacao do numero de ouro foi {abs(dec((a[len(a)-1]/a[len(a)-2])))}!")

#exec(open("fibonacci.py").read())