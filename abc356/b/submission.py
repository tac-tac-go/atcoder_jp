import numpy as np
n,m = map(int,input().split())
A_arr = list(map(int,input().split()))
X_arr = np.array([list(map(int,input().split())) for i in range(n)])
flag = True
for i in range(m):
  if sum(X_arr[:,i])>=A_arr[i]:
    continue
  else:
    flag = False
    break
print("Yes") if flag else print("No")
    

