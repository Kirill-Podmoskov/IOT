melt = {'Sn': 232, 'Zn': 420, 'Fe': 1539, 'Ni':
1455,'Si': 1415, 'Be': 1287}

values = input("Напиши два элемента через пробел ")
a,b = values.split()
t_1 = melt[a]
t_2 = melt[b]

print(f"Разница температур плавления {t_1-t_2}")