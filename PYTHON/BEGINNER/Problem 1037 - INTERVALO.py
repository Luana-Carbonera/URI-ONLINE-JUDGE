'''
Você deve fazer um programa que leia um número de ponto flutuante e imprima uma mensagem dizendo
em qual dos seguintes intervalos o número pertence: [0,25] (25,50], (50,75], (75,100). número for menor
 que zero ou maior que 100, o programa deve imprimir a mensagem “Fora de intervalo” que significa “Fora
 de intervalo”.

O símbolo '(' representa maior que. Por exemplo:
[0,25] indica números entre 0 e 25,0000, incluindo ambos.
(25,50] indica números maiores que 25 (25,00001) até 50,0000000.

Entrada
O arquivo de entrada contém um número de ponto flutuante.

Resultado
A saída deve ser uma mensagem como o exemplo a seguir.
'''

n = float(input())

if n >= 0 and n <= 25:
    print("Intervalo [0,25]")
elif n > 25 and n <= 50:
    print("Intervalo (25,50]")
elif n > 50 and n <= 75:
    print("Intervalo (50,75]")
elif n > 75 and n <= 100:
    print("Intervalo (75,100]")
elif n > 100 or n < 0:
    print("Fora de intervalo")