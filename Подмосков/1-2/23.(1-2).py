def my_filter(a):
  result = [str(x * 10) for x in a]  
  return " ".join(result)  

a = [-3,7,2,-10,-9,-2,5,8,4,5]
result = my_filter(a)
print(result)  
