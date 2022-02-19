"""
Faca um programa que leia algo pelo teclado e mostre
na tela seu tipo primitivo e todas as informacoes
possiveis sobre ele
"""

a = (input('Digite um valor: '))
print('O tipo primitivo desse valor é: ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('Está em maísculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está capitalizada? ', a.istitle())





