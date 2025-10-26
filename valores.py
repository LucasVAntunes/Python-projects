val = 0
resultado = 0

while True:
    soma = int (input ('Digite os valores a serem somados (999 para parar) '))
    if soma == 999:    
        break
    resultado += soma
    val += 1
    
print (f'O resultado das {val} somas é igual a: {resultado}')