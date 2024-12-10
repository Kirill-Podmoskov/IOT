#№25
def function(a = 1, b = 2, c = 3):
 return int(a + b / c)
x = function(2, c = 1, b = 2) 
print(x)

#№26
def func(*args):
  lst = []
  for item in args:
    if item % 2 == 0:
      lst.append(item)
  return lst

a, *b, c = func(1, 2, 3, 4, 5, 6, 7, 8)
print(b)