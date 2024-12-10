def volume(x,y,z):
    space = x*y
    if z !=0:
        result = space*z
    else:
        result = space
    return result

size = input("Введите размеры через пробел ")
x,y,z=size.split()
x=int(x)
y=int(y)
z=int(z)

result = volume(x, y, z)
print(result)