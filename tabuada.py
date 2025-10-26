n1 = int (input ('Deseja ver a tabuada de qual valor? '))
n2 = 0

while n2 <=10:
    if n1 < 0:
        break
    print(f'{n1} X {n2} = {n1 * n2}')
    n2 += 1