# VETORES (array unidimensional):

# 1. Escreva um programa que leia 10 valores inteiros e armazene em uma lista. O pro-
# grama deve imprimir no terminal quantos valores pares foram digitados pelo usuário.
# Dica: use o operador “%” para verificar se o número é par (ZERO é neutro, ZERO NÃO
# É PAR). Exemplos:
# Entrada 1:
# 1 7 3 2 3 6 4
# 8 5 5

# Saída 1:
# Qtd valores par: 4

# Entrada 2:
# 3 0 5 7 9 0 2
# 20 1 6

# Saída 2:
# Qtd valores par: 3

#RESOLUÇÃO: 
# lista = []
# n_pares = 0
# inteiros = input("Insira 10 números inteiros, separados por espaço, para adicionar à lista: ")
# for x in inteiros:
#     if x != " ":
#         lista += [int(x)]

# for x in lista:
#     if x%2 == 0:
#         n_pares += 1
# print (f"A quantidade de valores pares da lista foi: {n_pares} ")


# 2. Escreva um programa que recebe como entrada valores inteiros para criar duas listas

# de mesmo tamanho. O tamanho das listas deverá ser definido pelo usuário. O pro-
# grama deverá somar os valores pares e ímpar de cada uma das listas. Em seguida,

# comparar as somas e informar qual dos somatórios é maior ou se há um empate.
# Exemplos:
# Entrada 1:
# 4
# 1 7 3 2
# 3 6 4 8

# Saída 1:
# Soma listaPar1: 2
# Soma listaPar2: 18
# listaPar1 < listaPar2
# Soma listaImpar1: 11
# Soma listaImpar2: 3
# listaImpar1 > listaImpar2

# Entrada 2:
# 3
# 3 3 3
# 9 0 4

# Saída 2:
# Soma listaPar1: 0
# Soma listaPar2: 4
# listaPar1 < listaPar2
# Soma listaImpar1: 9
# Soma listaImpar2: 9
# listaImpar1 = listaImpar2

#Resolução: 
# soma_impar1 = 0
# soma_par1 = 0
# soma_impar2 = 0
# soma_par2 = 0
# lista1 = []
# lista2 = []
# tamanho_lista = int(input("Insira o tamanho das listas: "))
# for i in range (tamanho_lista):
#     valores1 = int(input())
#     lista1 += [valores1]
# print (f"A lista 1 é: {lista1}.")

# for i in range (tamanho_lista):
#     valores2 = int(input())
#     lista2 += [valores2]
# print (f"A lista 2 é: {lista2}.")

# for x in lista1:
#     if x%2 == 0:
#         soma_par1 += x
#     else:
#         soma_impar1 += x
# print (f"Soma lista Par1: {soma_par1} \n Soma lista Impar1: {soma_impar1}")

# for y in lista2:
#     if y%2 == 0:
#         soma_par2 += y
#     else:
#         soma_impar2 += y
# print (f"Soma lista Par2: {soma_par2} \n Soma lista Impar2: {soma_impar2}")

# if soma_par1>soma_par2:
#     print("ListaPar1>ListaPar2")
# else:
#     print("ListaPar2>ListaPar1")

# if soma_impar1>soma_impar2:
#     print("ListaImpar1>ListaImpar2")
# else:
#     print("ListaImpar2>ListaImpar1")

###################################################################################################

# 3. leia 10 valores inteiros e armazene em uma lista. O programa deve imprimir no terminal
# quantos valores pares foram digitados pelo usuário. Dica: use o operador “%” para
# verificar se o número é par (ZERO é neutro, ZERO NÃO É PAR). Exemplos:
# Entrada 1:
# 1 7 3 2 3 6 4
# 8 5 5

# Saída 1:

# Quantidade de valo-
# res par: 4

# Entrada 2:
# 3 0 5 7 9 0 2
# 20 1 6

# Saída 2:
# Quantidade de valores
# par: 3

#RESOLUÇÃO:

# lista = []
# n_pares = 0

# for x in range (10):
#     valores = int(input("Insira 10 números: "))
#     lista.append(valores)
# print (lista)

# for valor in lista:
#     if valor % 2 == 0:
#         n_pares += 1
# print (f"A quantidade de números pares na lista foi de: {n_pares}")

############################################################################

# 4. Escreva um programa que receba como entrada 3 parâmetros: um valor inteiro corres-
# pondente à quantidade de elementos de dois arrays unidimensionais; duas sequências

# de valores do tamanho do primeiro parâmetro, os quais deverão ser armazenados em
# duas listas distintas. Em seguida, o programa deverá criar uma lista resultante formada
# pela intercalação dos valores de cada uma das sequências de entrada. Como saída o
# programa deverá imprimir as duas listas iniciais e a lista resultante. Exemplo:
# Entrada:
# 3
# ‘a’ True 20
# ‘b’ ‘c’ 30

# Saída:
# lista1 = [‘a’, True, 20]
# lista2 = [‘b’, ‘c’, 30]
# lista3 = [‘a’, ‘b’, True, ‘c’, 20, 30]

#RESOLUÇÃO:
# lista1 = []
# lista2 = []
# quantidade_elementos = int(input("Insira a quantidade de elementos das listas posteriores: "))
# for x in range (quantidade_elementos):
#     elementos1 = input()
#     lista1.append(elementos1)
#     elementos2 = input()
#     lista2.append(elementos2)
# print(lista1)
# print(lista2)
# lista3 = [lista1+lista2]
# print(lista3)

###################################################################################################

# 5. Escreva um programa que receba como entrada uma sequência de valores inteiros.
# Para tanto, o programa deverá inicialmente solicitar ao usuário quantos valores serão
# fornecidos para análise e só depois solicitar os valores a serem analisados. A análise
# consistirá em identificar e apresentar a partir da sequência de valores fornecidos, o
# menor valor, o maior valor e a média aritmética dos valores. Exemplos:
# Entrada 1:
# 7
# 1 9 3 2 3 6 4

# Saída 1:
# Menor valor: 1
# Maior valor: 9
# Média aritmética: 4

# Entrada 2:
# 3
# 10 40 13

# Saída 2:
# Menor valor: 3
# Maior valor: 40
# Média aritmética: 21


#RESOLUÇÃO:
# lista_valores = []
# quantidade_de_valores = int(input())

# for x in range (quantidade_de_valores):
#     valores = int(input("Adicione valores inteiros: "))
#     lista_valores.append(valores)
# menor_valor = min(lista_valores)
# maior_valor = max(lista_valores)
# media_aritmetica = sum(lista_valores)/quantidade_de_valores
# print (f"O menor valor é: {menor_valor}")
# print (f"O maior valor é: {maior_valor}")
# print(f"A média aritmética da lista é: {media_aritmetica}")

##########################################################################

# 6. Crie um programa que solicite ao usuário uma lista de números inteiros e uma string
# de mesmo comprimento. O programa deve substituir os números nos índices ímpares

# da lista por caracteres correspondentes da string nos mesmos índices. Exiba a se-
# quência resultante, separada por um espaço em branco. Exemplo:

# Entrada:
# 1 2 3 4 5 6
# abcdef

# Saída:
# 1 b 3 d 5 f

#RESOLUÇÃO: 

# numeros = input("Digite uma lista de números separados por espaço: ").split()
# string = input("Digite uma string com o mesmo número de caracteres: ")


# if len(numeros) != len(string):
#     print("A lista de números e a string devem ter o mesmo comprimento.")
# else:
    
#     resultado = []
    
#     for i in range(len(numeros)):
#         if i % 2 == 1:
#             resultado.append(string[i])
#         else:
#             resultado.append(numeros[i])
#             print(resultado)

########################################################################

#8. Escreva um programa que receba como entrada uma string constituída por uma se-
# quência de números inteiros separados por espaço. O programa deverá transformar

# essa string em uma lista de números inteiros e apresentar o resultado da soma dos
# valores das posições ímpares dessa lista. Exemplos:
# Entrada 1:
# 1 9 3 2 3 9 4

# Saída 1:
# 9+2+9 = 20

# Entrada 2:
# 10 40 13 5 8 12 15 13

# Saída 2: 40+5+12+13=70

#RESOLUÇÃO: 
# soma = 0
# operacao = ""

# n_strings = input("Digite uma sequênca de números inteiros separados por espaço: ")
# lista_inteiros = list(map(int, n_strings.split()))

# for i in range (1, len(lista_inteiros), 2):
#     soma += lista_inteiros[i]
#     operacao += str(lista_inteiros[i]) + " + "

# operacao = operacao[:-2] + f" = {soma}"
# print(operacao)

#######################################################################


# 9. Escreva um programa que receba como entrada uma string várias palavras separadas
# por espaço. O programa deverá verificar e apresentar a quantidade de ocorrência de
# cada palavra no texto repassado como entrada para o programa. Os sinais de pontu-
# ação não devem ser contabilizados, como por exemplo “.” Ou “,”.


#RESOLUÇÃO:
contador = 0
lista_de_palavras = []

string = input("Insira palavras separadas por espaço: ")
lista_de_palavras = string.split(" ")

lista_tratadas = []

#Remove a pontuação
for palavra in lista_de_palavras:
    if "." in palavra or "," in palavra:
        lista_tratadas += [palavra[:-1]]

lista_unicas = []
for palavra in lista_tratadas:
    if palavra not in lista_unicas:
        lista_unicas += [palavra]

lista_quantidade = [ 0 for _ in range (len(lista_unicas))]
i = 0
for unica in lista_unicas:
    for palavra in lista_tratadas:
        if unica == palavra:
            lista_quantidade[i] += 1
    i += 1

print("Relação de palavras e quantidade: ")
for i in range(len(lista_unicas)):
    print(f"{lista_unicas[i]}={lista_quantidade[i]};")







