#6
s = "change me"
x = s.replace("e", "E")
print(x)
#7
str_1 = "red"
str_2 = "white"
str_3 = "green"
print(str_1 + str_2)
#redwhite
print("_".join([str_1, str_2]))
#red_white
print("_".join([str_1, str_3]))
#red_green
print(str_3.find("a"))
#-1
print(str_2.find("e"))
#4
print(str_3.split("r"))
#['g', 'een']