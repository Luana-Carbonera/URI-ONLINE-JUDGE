'''
Usando a tabela a seguir, escreva um programa que leia um código e a quantidade de um item.
Após, imprima o valor a pagar. Este é um programa muito simples com o único intuito de praticar comandos
de seleção.

Entrada
O arquivo de entrada contém dois números inteiros X e Y . X é o código do produto e Y é a
quantidade deste item de acordo com a tabela acima.

Resultado
A saída deve ser uma mensagem "Total: R$ " seguida do valor total a ser pago, com 2 dígitos após a vírgula.


'''

x, y = input().split()
x = int(x)
y = int(y)

if x == 1:
    print("Total: R$", '%.2f'%(y * 4.00))
elif x == 2:
    print("Total: R$", '%.2f'%(4.50 * y))
elif x == 3:
    print("Total: R$", '%.2f'%(5.00 * y))
elif x == 4:
    print("Total: R$", '%.2f'%(2.00 * y))
elif x == 5:
    print("Total: R$", '%.2f'%(1.50 * y))
