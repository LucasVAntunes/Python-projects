n = (input ('Digite um número de 0 a 9999: '))

print (f'UNIDADES: {n[(len(n))-1]}')

if ((len (n)) > 1):

    print (f'DEZENAS: {n[(len(n))-2]}')

if ((len (n)) > 2):

    print (f'CENTENAS: {n[(len(n))-3]}')

if ((len (n)) > 3):

    print (f'MILHARES: {n[(len(n))-4]}')
