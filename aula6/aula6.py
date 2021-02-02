"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""

nome = 'Jefferson Oliveira'
idade = 29  # int
altura = 1.90  # float
eMaior = idade > 18  # bool
peso = 87.0  # float
imc = peso/altura**2

print(nome, 'tem', idade, 'anos de idade e seu IMC é', imc)
