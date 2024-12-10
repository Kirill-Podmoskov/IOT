letters = {'a': 1, 'b': 2, 'c': 3, 'd':
4,'e': 5, 'f': 6,'g':7,'h':8}
    
coord = input("Координаты клетки на доске")
hor_pos=letters[coord[0]]
ver_pos=int(coord[1])

if (ver_pos+hor_pos)%2==0:
    print("Цвет - Black")
else:
    print("Цвет - White")