"""
Operadores Lógicos
and, or, not
in e not in

a = ''
b = 0

if not a:
    print('Ta errado')


nome = 'Welton Carvalho'

if 'n' in nome:
    print('ta aqui')

if 'w' not in nome:
    print('Aqui tbm')
"""

usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_db = 'Welton'
senha_db = '123456'

if usuario_db == usuario and senha_db == senha:
    print('Você está logado')
else:
    print('Você não está logado')
