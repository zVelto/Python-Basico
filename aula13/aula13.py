usuario = input('Digite seu usuário: ')
qtd_caractere = len(usuario)

if qtd_caractere < 6:
    print('Você passou')
else:
    print('você não passou')
