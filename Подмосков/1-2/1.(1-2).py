import math
room = int(input("Номер квартиры= "))
if room % 8 == 0:
  floor = 8
  entrance = math.floor(room / 8)
else:
  floor = room % 8
  entrance = math.floor(room / 8) + 1
print(f"Этаж: {floor}, Подъезд: {entrance}")