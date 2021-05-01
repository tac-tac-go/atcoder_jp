import string
import numpy as np
h,w = map(int,input().split())
col = list(string.ascii_uppercase)
row = list(range(1,h+1))
array = np.array([input().split() for i in range(h)])
for i in range(h):
  for j in range(w):
    if array[i,j]=="snuke":
      print(str(col[j])+str(row[i]))
      break