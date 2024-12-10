import math
x = float(input("Введите значение X"))

sum = 0 
n = 1
term=x
while abs(term) >= 1e-6:
    sum += term
    n += 1
    term = (-1)**(n+1) * x**n / n
a = round(sum,8)

print(a)