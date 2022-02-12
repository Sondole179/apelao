from math import cos
from decimal import * 
getcontext().prec = 1000

pi = 0
for i in range(100000):
    if i % 2 == 0: pi += Decimal(4)/Decimal(2*i + 1)
    else: pi -= Decimal(4)/Decimal(2*i + 1)
print(pi)

#exec(open('pi.py').read())