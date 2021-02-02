nome = 'Jefferson Oliveira'
idade = 29  # int
altura = 1.90  # float
eMaior = idade > 18  # bool
peso = 87.0  # float
imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos de idade e seu IMC é', imc)
print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}')
print('{0} tem {1} anos e seu IMC é {2}'.format(nome, idade, imc))
print('{n} tem {i} anos e seu IMC é {c}'.format(n=nome, i=idade, c=imc))
