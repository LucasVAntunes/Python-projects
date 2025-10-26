ext = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco')
n = int (input ("Digite um número entre 0 e 5: "))

while n > 6 & n < 0:
    n = int (input ("Tente novamente. Digite um número entre 0 e 5"))

print (f'Você digitou o número {ext[n]}')