# lista = []
# consoantes = 0
# print ('Informe os caracteres')
# for i in range(10):
#     lista.append((input('Caracter  ' + str(i + 1) + ':\n')))
#     char = lista[i]
# if(lista not in ('a','e','i','o','u')):
#     print(consoantes)
lista = []

for i in range(1, 11):

    letra = input('Digite vocais e consoante')
    lista.append(letra)

contador = 0

for item in lista:
    if item == 'a' or item == 'e' or item == 'i' or item == 'o' or item =='u':
        pass

    else:
        print(item)
        contador = contador + 1

print(contador)

"""

SOLUÇÃO ALTERNATIVA USANDO NOT IN

for item in lista:

    if item not in ['a','e','i','o','u']:
        print(item)
        contador = contador + 1
print(contador)
"""