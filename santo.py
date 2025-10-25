city = input ('Qual o nome da sua cidade: ')
city.strip()

if ((city.lower().find('santo'))== 0):
    print ('A sua cidade começa com SANTO')
else:
    print ('A sua cidade não começa com SANTO')