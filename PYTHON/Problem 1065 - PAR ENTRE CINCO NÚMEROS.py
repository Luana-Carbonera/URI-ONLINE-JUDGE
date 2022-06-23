'''
Faça um programa que leia cinco valores inteiros .
Conte quantos  desses valores são pares e imprima essas informações como no exemplo a seguir .

Entrada
A entrada será de 5 valores inteiros.

Resultado
Imprima uma mensagem como o exemplo a seguir com todas as letras em minúsculas,
indicando quantos números pares foram digitados.
'''

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
par = 0
impar = 0

if a % 2 == 0:
    par = par + 1
else:
    impar
if b % 2 == 0:
    par = par + 1
else:
    impar
if c % 2 == 0:
    par = par + 1
else:
    impar
if d % 2 == 0:
    par = par + 1
else:
    impar
if e % 2 == 0:
    par = par + 1
else:
    impar

print(par, "valores pares")