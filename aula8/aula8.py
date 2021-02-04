nome = 'Welton'
idade = 25
altura = 1.73
anoAtual = 2020
peso = 80  

anoNascimento = anoAtual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {anoNascimento}.')
