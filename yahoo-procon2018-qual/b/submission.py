import math
x, k = map(int, input().split())
min_val = int("1"+("0")*k)
if min_val >= x+1:
  print(min_val)
else:
  print((math.ceil((x+1)/min_val))*min_val)
