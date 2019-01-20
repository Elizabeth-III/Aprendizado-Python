Nessa pasta senhoras e senhores, vocês vão encontrar soluções para algumas das questões [dessa lista](https://wiki.python.org.br/EstruturaDeRepeticao) de exercícios.

#### Algoritmos

##### Exercício 1
1. Loop eterno
   1. Receba um número inteiro do usuário e guarde em uma variável
   2. Se a nota for maior ou igual a 0 E a nota for menor ou igual a 10
      1. Saia do loop eterno
   3. Senão
      1. Imprima "A nota digitada é inválida!" 
2. Imprima "A nota <valordanota> é válida"
##### Exercício 2
1. Loop eterno
   1. Pergunte o nome do usuário e guarde em uma variável
   2. Pergunte a senha do usuário e guarde em uma variável
   3. Se o usuário for igual à senha
      1. Imprima "Erro, tente novamente."
   4. Senão
      1. Imprima sucesso
      2. Saia do loop eterno
##### Exercício 3
1. Loop eterno
   1. Pergunte o nome ao usuário e guarde em uma variável
   2. Pergunte a idade ao usuário e guarde em uma variável
   3. Pergunte o salário ao usuário e guarde em uma variável
   4. Pergunte o sexo ao usuário e guarde em uma variável
   5. Se o tamanho do nome for maior que 3
      1. Se a idade for maior que 0 E a idade for menor ou igual a 150
         1. Se o salário for maior que 0
            1. Se o sexo for igual a 'f' ou 'F' ou 'm' ou 'M'
               1. Se o estado civil for 's' ou 'c' ou 'v' ou 'd'
                  1. Imprima "Tudo OK"
                  2. Saia do loop infinito
               2. Senão
                  1. Imprima "Estado civil inválido"
            2. Senão
               1. Imprima "Sexo inválido"
         2. Senão
            1. Imprima "Salário inválido"
      2. Senão
         1. Imprima "Idade inválida"
   2. Senão
      1. Nome inválido             

#####Exercício 4

1. Defina a quantidade de habitantes da população A e B
   1.Defina também o percentual de crescimento da população A e B
2. Enquanto população A menor que população B
   1. Anos é igual a anos + 1
   2. Faça a soma de população A igual População A + (população A * crescimento A)
   3. Faça o mesmo para população B
3. Imprima a porcentagem de crescimento de maior valor
   1. Imprima os valores finais da população A e B.
   
   
#####Exercício 5 


1. Informe a população da cidade A em decimal
2. Informe a população da cidade B em decimal
3. O ano é = à zero
4. Informe a taxa de crescimento em decimal da população A
5. Informe também a taxa de crescimento em decimal da população B
6. Enquanto a população A < que a população B:
   1. População A + = round, faça 'população A * Taxa de crescimento A entre parenteses e por fim divida por 100'
   2. População B + = round, faça população B * taxa de crescimento B, entre parenteses e o divida por 100
7. ano é = a ano + 1
8. Imprima quantos anos levará para a cidade A ser maior que a B.
9. Imprima população B terá x habitantes
10. Imprima população A terá x habitantes.


#####Exercício 6

1. Para i de 1 até 21: 
   1. imprima i
2. número + espaço + espaço + espaço (...) até 21.




#####Exercício 7

1. Primeiro, peça um número e guarde numa variável
2. Peça o segundo número e guarde também na variável
3. Se o primeiro > que o segundo
   1. então imprima e guarde primeiro
2. Se não,
   1. imprima e guarde o segundo
12. Para i de de 1 até 6
    1.  Peça o terceiro número e guarde numa variável
        5. Se o número  informado é maior do que o já salvo
           1. imprima e guarde
        2. Se não, 
           1. Ignore e continuo com o número já salvo
           
           
#####Exercício 8

1. Comece pedindo ao usuário que digite 5 números decimais e os guarde numa variável
2. Na variável denominada "soma" some todos os cinco números usando + para isso.
3. Imprima "soma" para a soma dos valores
4. Imprima "média" para a soma divido por 5.


#####Exercício 9

1. Para i de 1 até 51, acrescente o número dois para que 
2. Imprima i


#####Exercício 10

1. Peça ao usuário que digite dois números e os salve respectivamente nas variáveis num1 e num2
2. Enquanto num2 < num1 então digite os números que está sendo pedido
3. Se não,
   1. Para i in range (num1, num2,1):
      print (i)