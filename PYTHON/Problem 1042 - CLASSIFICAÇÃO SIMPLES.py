'''
Leia três números inteiros e ordene-os em ordem crescente.
Após, imprima esses valores em ordem crescente, uma linha em branco
e depois os valores na sequência conforme foram lidos.

Entrada
A entrada contém três números inteiros.

Resultado
Apresente a saída conforme solicitado acima.
'''

a1,b1,c1 = input().split()
a1 = int(a1)
b1 = int(b1)
c1 = int(c1)

if a1 > b1 and a1 > c1:
    d = a1
    if b1 > c1:
        e = b1
        f = c1
    else:
        e = c1
        f = b1

if b1 > a1 and b1 > c1:
    d = b1
    if a1 > c1:
        e = a1
        f = c1
    else:
        e = c1
        f = a1

if c1 > a1 and c1 > b1:
    d = c1
    if a1 > b1:
        e = a1
        f = b1
    else:
        e = b1
        f = a1

print(f)
print(e)
print(d)
print("")
print(a1)
print(b1)
print(c1)