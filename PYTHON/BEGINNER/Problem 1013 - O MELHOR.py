valor = input().split(" ")

a, b, c = valor

MAIOR = (int(a)+int(b)+abs(int(a)-int(b))) / 2
RESULTADO = (int(MAIOR) + int(c) + abs(int(MAIOR) - int(c)))/2

print("%d eh o maior" % RESULTADO)
