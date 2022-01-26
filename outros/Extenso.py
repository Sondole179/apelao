def por_extenso(numero): 
    numero = [int(i) for i in list(f'{numero}')]
    extenso = ''
    n = 0
    for l in range(len(numero)):
        if numero[l] != 0:
            if (len(numero)-l) % 3 == 0:
                extenso += ['cento','duzentos','trezentos','quatrocentos','quinhentos','seiscentos','setecentos','oitocentos','novecentos'][numero[l]-1]
            if (len(numero)-l) % 3 == 2:
                if numero[l] > 1:
                    extenso += ['vinte','trinta','quarenta','cinquenta','sessenta','setenta','oitenta','noventa'][numero[l]-2]
                else:
                    extenso += ['dez','onze','doze','treze','quatorze','quinze','dezessei','dezessete','dezoito','dezenove'][numero[l+1]]
                    n = 1
            if (len(numero)-l) % 3 == 1 and n == 0:
                extenso += ['um','dois','tres','quatro','cinco','seis','sete','oito','nove'][numero[l]-1]
        if (len(numero)-l) % 3 == 1:
            n = 0
            extenso += ['',' mil',' milhoes','bilhoes','trilhoes'][int((len(numero)-l)/3)]
        if l != len(numero)-1 and numero[l] != 0 and numero[l+1] != 0 and n == 0:
            extenso += ' e '

    return extenso

print(por_extenso(123456789123456))
#exec(open('Extenso.py').read())