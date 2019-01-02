'''
Faça um programa que pergunte o preço de três produtos e informe qual produto
você deve comprar, sabendo que a decisão é sempre pelo mais barato.
'''

num1 = int(input('Primeiro número'))
num2 = int(input('Segundo número'))
num3 = int(input('Terceiro número'))
if num1 < num2 < num3:
    print('O menor número é: {}'.format(num1))
elif num2 < num1 <num3:
    print('O menor número é: {}'.format(num2))
else:
    print('O menor número é: {}'.format(num3))