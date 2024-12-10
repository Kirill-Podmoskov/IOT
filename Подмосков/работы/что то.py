file = open('data.txt')
s = 0
for line in file:
    for i in line.split():
        s = s + int(i)
print(s)