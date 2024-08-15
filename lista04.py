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





