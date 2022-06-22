time = int(input())

horas = (time / 3600)
sobra = (time % 3600)
minutos = (sobra / 60)
segundos = (sobra % 60)
print(repr(int(horas)) + ":" + repr(int(minutos)) + ":" + repr(int(segundos)))