import math
def trapz(func, a, b, N):
   
    step = (b - a) / N 
    result = 0.5 * (func(a) + func(b)) 

    for i in range(1, N):
        x = a + i * step  
        result += func(x)  

    return round(result * step, 8)  

func_str = input("Напишите функцию интегрирования : ")
func = eval(func_str)

data = input("Напишите начальное значение, конечное значение и количество точек через пробел: ")
a, b, N = map(int, data.split())

result = trapz(func, a, b, N)
print(f"Приближенное значение интеграла: {result}")