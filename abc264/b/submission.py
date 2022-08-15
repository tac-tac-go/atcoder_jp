import numpy as np

array = np.array([[1]])
for i in range(7):
  if i%2==0:
    array = np.pad(array, (1, 1), constant_values=0)
  else:
    array = np.pad(array, (1, 1), constant_values=1)
r,c = map(int,input().split())
print("black") if array[r-1,c-1]==0 else print("white")
    
    
