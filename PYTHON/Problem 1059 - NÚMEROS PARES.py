'''
Escreva um programa que imprima todos os números pares entre 1 e 100, incluindo-os se for o caso.

Entrada
Neste problema extremamente simples não há entrada.

Resultado
Imprima todos os números pares entre 1 e 100, incluindo-os, um por linha.
'''

for i in range(1, 101):
    if i % 2 == 0:
        print(i)
