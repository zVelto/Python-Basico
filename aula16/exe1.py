num1 = input("Digite um número inteiro: ")

if num1.isdigit():

    num1 = int(num1)

    if num1 % 2 == 0:
        print(f'O número {num1} é par')
    else:
        print(f'O número {num1} é impar')
else:
    print(f'{num1} não é um número inteiro')
