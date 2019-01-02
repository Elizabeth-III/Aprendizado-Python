#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num1=int( input('Digite o primeiro numero: ') )
num2=int( input('Digite o segundo numero: ') )

if num1 > num2 :
    print('O primeiro, %d, é maior' %num1)
else:
    if num1 == num2 :
        print('Os números são iguais')
    else:
        print('O segundo, %d, é maior' %num2)
