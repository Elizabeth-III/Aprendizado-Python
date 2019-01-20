# Faça um programa que leia 5 números e informe o maior número

num1 = int(input('Primeiro número'))
num2 = int(input('Segundo número'))
if num1 > num2:
    print ('O maior número é o {}'.format(num1))
    maior = num1
else:
    print ('O maior número é o {}'.format(num2))
    maior = num2

for i in range(1,6):
    num3 = int(input('Digite outro número'))
    if num3 > maior:


        maior = num3


print('O número {} é o maior'.format(maior))
