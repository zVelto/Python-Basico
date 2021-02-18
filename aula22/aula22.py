# texto = 'Python'
#
# for letra in texto:
#     print(letra)

# for numero in range(20, 10, -2):
#     print(numero)
#
# for numero in range(0, 100, 8):
#     print(numero)

# for n in range(100):
#     if n % 8 == 0:
#         print(n)

# continue - pula para o próximo laço
# break - termina o laço

texto = 'python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string += letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra

print(nova_string)
