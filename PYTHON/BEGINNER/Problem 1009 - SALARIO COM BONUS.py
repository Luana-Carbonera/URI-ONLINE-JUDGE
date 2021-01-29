# -- coding: utf-8 --

name = input()
salary = float(input())
sale = float(input())
bonus = float((sale * 15) / (100))
vencimento = (salary + bonus)

print("TOTAL = R$ %0.2f" %vencimento)