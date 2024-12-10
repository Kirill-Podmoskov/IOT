coord = input("Напишите координаты точки X,Y через пробел ")
x,y = coord.split()
x=int(x)
y=int(y)

if (x-1)^2+y^2<=4 and (x-1)^2+y^2>=1:
    cicle= "yes"
else:
    cicle= "no"

if abs(x-4)<=2 and abs(y-2)<=3:
    square = "yes"
else:
    square = "no"
print(f"Точка попадает в кольцо? {cicle} Точка попадает в квадрат? {square}")