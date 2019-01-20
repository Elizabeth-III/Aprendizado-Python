# criação de uma lista com 4 itens
lista = [1,'banana', 'baby', 0.8]
print (lista)
# loop que itera cada item da lista
for item in lista:
    print (item)
#Criação de lista vazia
lista = []
#Adição do número 1 na lista
lista.append(1)
print (lista)
lista.append('banana')
print(lista)
lista.append('baby')
print(lista)
lista.append('0,8')
print(lista)
#Acessar o segundo item da lista
print(lista[1])
#Acessar do terceiro item da lista pra frente
print(lista[2:])
#Acessar até o terceiro item da lista


print(lista[:2])
#Acessar o segundo e o terceiro item da lista
print(lista[1:3])
#Acessar o último item da lista
print(lista[:-1])
#Acessar os três últimos itens da lista
print(lista[:-3])
lista1 = ['eu', 'amo', 'você']
lista2 = ['era', 'mentira', 'feio']
#Criação de uma lista com duas listas dentro
lista = [lista1, lista2]
print (lista)
#Loop que itera cada item de cada uma das listas dentro da lista
for l in lista:
    print(l)
    for item in l:
        print (item)