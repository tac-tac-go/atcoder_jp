import math
n = int(input())
floor = math.floor(n/5)*5
ceil = math.ceil(n/5)*5
if abs(n-floor)<abs(n-ceil):
  print(floor) 
else:
  print(ceil)
