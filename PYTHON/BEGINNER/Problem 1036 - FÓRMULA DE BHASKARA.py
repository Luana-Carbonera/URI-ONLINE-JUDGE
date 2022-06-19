'''
Leia 3 números de ponto flutuante.
Depois, imprima as raízes da fórmula de bhaskara.
Se for impossível calcular as raízes por divisão por zero ou raiz
quadrada de um número negativo, apresenta a mensagem “Impossivel calcular” .

Entrada
Leia 3 números de ponto flutuante (duplo) A, B e C.

Resultado
Imprima o resultado com 5 dígitos após o ponto decimal ou a mensagem
se for impossível calcular.
'''

a1,b1,c1=list(map(float,input().split()))

delta = (b1 ** 2) - 4 * a1 * c1

if a1 == 0:
    print("Impossivel calcular")
elif delta < 0:
    print("Impossivel calcular")
else:
    x1 = (-b1 + delta ** (1 / 2)) / (2 * a1)
    x2 = (-b1 - delta ** (1 / 2)) / (2 * a1)
    print("r1 =","%0.5f"%x1)
    print("r2 =","%0.5f"%x2)




