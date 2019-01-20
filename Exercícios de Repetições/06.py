# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.

x = 0
for i in range(1, 21):
	x = x + i

for i in range (1,21):
	print (i)

e = ""
for i in range(1, 21):
	e = e + str(i) + ' '

print(e)