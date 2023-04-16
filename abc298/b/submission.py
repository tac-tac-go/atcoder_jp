import numpy as np
import sys
n = int(input())
array1 = np.array([list(map(int,input().split())) for i in range(n)])
array2 = np.array([list(map(int,input().split())) for i in range(n)])
mt1 = np.where(array1==1)
flag1 = True
for i,j in zip(mt1[0],mt1[1]):
  if array2[i,j]==0:
    flag1 = False
    break

flag2 = True
mt2 = np.where(np.rot90(array1, -1)==1)
for i,j in zip(mt2[0],mt2[1]):
  if array2[i,j]==0:
    flag2 = False
    break
    
flag3 = True
mt3 = np.where(np.rot90(array1, -2)==1)
for i,j in zip(mt3[0],mt3[1]):
  if array2[i,j]==0:
    flag3 = False
    break

flag4 = True
mt4 = np.where(np.rot90(array1, -3)==1)
for i,j in zip(mt4[0],mt4[1]):
  if array2[i,j]==0:
    flag4 = False
    break

print("Yes") if np.array([flag1,flag2,flag3,flag4]).any() else print("No")

