s = int(input())
a = int(input())
b = int(input())
import math
if s-a<=0:
  print(250)
else:
  print(250+(math.ceil((s-a)/b))*100)
  
