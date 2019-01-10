# Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = int(input('Primeiro número'))
num2 = int(input('Segundo número'))
num3 = int(input('Terceiro número'))
if num1 > num2 > num3:
    print('O maior número é o {}'.format(num1))
if num2 > num3 > num1:
    print('O maior número é o {}'.format(num2))
if num3 > num2 > num1:
    print('O maior número é o {}'.format(num3))
if num1 > num2 and num1 < num3:
    print('O número {} é o do meio'.format(num1))
if num1 < num2 and num1 > num3:
    print('O número {} é o do meio'.format(num1))
if num2 > num1 and num2 < num3:
    print('O número {} é o do meio'.format(num2))
if num2 < num1 and num2 > num3:
    print('O número {} é o do meio'.format(num2))
if num3 > num1 and num3 < num2:
    print('O número {} é o do meio'.format(num3))
if num3 < num1 and num3 > num2:
    print('O número {} é o do meio'.format(num3))
if num1 < num2 < num3:
    print('O número {} é o menor'.format(num1))
if num2 < num3 < num1:
    print('O número {} é o menor'.format(num2))
if num3 < num2 <num1:
    print('O número {} é o menor'.format(num3))