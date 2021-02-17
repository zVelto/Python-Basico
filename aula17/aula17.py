num1 = 10
num2 = 2548

"""
divisao = num1 / num2
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

nome = 'Welton Carvalho'
print(f'{nome:s}')

print(f'{num1:0>10}')
print(f'{num2:0^10}')
print(f'{num2:0<10}')

print(f'{num2:.2f}')
print(f'{num2:0>10.2f}')

nome = 'Welton Carvalho'

print(f'{nome:#^50}')

nome = 'Welton Carvalho'
# nome_formatado = '{:@>10}'.format(nome)
nome_formatado = '{n:@>20}'.format(n=nome)
nome_formatado2 = '{n:0<20}'.format(n=nome)
print(nome_formatado)
print(nome_formatado2)
"""
nome = 'Welton'
sobrenome = 'Carvalho'

nome_formatado = '{0:U<40}{1:Y^50}'.format(nome, sobrenome)
nome_formatado2 = nome.ljust(20, 'C')

print(nome_formatado2)
