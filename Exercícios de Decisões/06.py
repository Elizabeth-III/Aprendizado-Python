# Faça um Programa que leia três números e mostre o maior deles.

num1 = int(input('Primeiro número'))
num2 = int(input('Segundo número'))
num3 = int(input('Terceiro número'))
if num1 > num2 > num3:
    print('O maior número é: {}'.format(num1))
elif num2 > num1 >num3:
    print('O maior número é: {}'.format(num2))
else:
    print('O maior número é: {}'.format(num3))