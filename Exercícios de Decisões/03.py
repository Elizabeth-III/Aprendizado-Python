'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido
'''

resposta=input('M ou F: ')

if resposta == 'm':
    print('Masculina')
elif resposta == 'f':
    print('Feminina')
else:
    print('Você não digitou M ou F')