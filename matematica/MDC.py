def MDC(a,b):
    while a != 0 and b != 0:
        if a > b: a %= b
        else: b %= a
    return(max(a,b))

def MMC(a,b):
    return(int(a*b/MDC(a,b)))

def mdc(li):
    for i in range(len(li)-1):
        li[i+1] = MDC(li[i],li[i+1])
    return(li[len(li)-1])

def mmc(li):
    for i in range(len(li)-1):
        li[i+1] = MMC(li[i],li[i+1])
    return(li[len(li)-1])

print(mmc([15,15,15,450]))
#exec(open('MDC.py').read())