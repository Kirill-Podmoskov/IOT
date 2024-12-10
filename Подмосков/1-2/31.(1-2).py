filename = "1.txt"
data = [(1, 20), (2, 30), (3, 40), (4, 35), (5, 22), (6, 10)]
with open(filename, 'w') as file:
        for time, value in data:
            file.write(f"{time}\t{value}\n")