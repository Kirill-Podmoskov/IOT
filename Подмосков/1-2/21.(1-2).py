pos = [1, 3, 4, 7, 8, 9, 10]
max_speed = 0

for i in range(len(pos) - 1):  
    if (pos[i + 1] - pos[i]) / 0.01 > max_speed and pos[i + 1] > 0:
        max_speed = (pos[i + 1] - pos[i]) / 0.01
print(f"Максимальная скорость = {max_speed}(нм/с)")
