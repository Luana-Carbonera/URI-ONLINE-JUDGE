n = int(input())

ano = (n // 365)
n = (n - (ano*365))

mes = (n // 30)
n = (n - (mes*30))

dia = n

print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(dia))