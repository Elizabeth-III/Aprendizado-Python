# num1 = float(input('Notas do 1º bimestre:'))
# num2 = float(input('Notas do 2º bimestre:'))
# num3 = float(input('Notas do 3º bimestre:'))
# num4 = float(input('Notas do 4º bimestre:'))
# print('A sua média foi:', (num1+num2+num3+num4)/4)
#
# lista = float(input('Nota do 1º bimestre: '))
# lista = float(input('Nota do 2º bimestre: '))
# lista = float(input('Nota do 3º bimestre: '))
# lista = float(input('Nota do 4º bimestre: '))
# print = (lista/4)


listaNotas = []
media = 0
print ('Informe as 4 notas')
for i in range(4):
	listaNotas.append(float(input('Nota '+ str(i+1) + ':\n')))
	media += listaNotas[i]
media = media/4
print (listaNotas)
print (media)