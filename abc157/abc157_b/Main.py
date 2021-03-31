import numpy as np
a = [list(map(int,input().split())) for i in range(3)]
n= int(input())
b = [int(input()) for i in range(n)]
for i in range(3):
  for j in range(3):
    if a[i][j] in b:
      a[i][j]=-1
a = np.array(a)
result="No"
for i in range(3):
  if len(set(a[:,i]))==1 or len(set(a[i,:]))==1:
      result="Yes"
  
if a[0,0]==a[1,1]==a[2,2]==-1:result="Yes"
if a[2,0]==a[1,1]==a[0,2]==-1:result="Yes"
print(result)