hora = int(input('Digite a hora: '))

if 0 <= hora <= 11:
    print('Bom dia!')
elif 11 < hora <= 17:
    print('Boa tarde!')
else:
    print('Boa noite!')
