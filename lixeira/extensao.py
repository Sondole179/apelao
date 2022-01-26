def ext(num):
    li = [int(j) for j in list(f'{num}')]
    extenso = []
    for i in range(len(li)):
        if li[i] != 0:
            if (len(li)-i) % 3 == 0: 
                extenso.append(['cento','duzentos','trezentos','quatrocentos','quinhentos','seiscentos','setecentos','oitocentos','novecentos'][li[i]-1])
            if (len(li)-i) % 3 == 2:
                if li[i] == 1: 
                    extenso.append(['dez','onze','doze','treze','quatorze','quinze','dezessei','dezessete','dezoito','dezenove'][li[i]])
                    n = 1
                else: 
                    extenso.append(['dez','vinte','trinta','quarenta','cinquenta','sessenta','setenta','oitenta','noventa'][li[i]-1])
            if (len(li)-i) % 3 == 1: 
                if n == 0: extenso.append(['um','dois','tres','quatro','cinco','seis','sete','oito','nove'][li[i]-1])
    return(extenso)

print(ext(11011))

#exec(open('extensao.py').read())