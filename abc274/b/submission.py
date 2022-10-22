H,W = map(int,input().split())
import numpy as np
array = np.array([list(input()) for i in range(H)])
result = []
for i in range(W):
  result.append(str(len(list(np.where(array[:,i]=="#")[0]))))
print(" ".join(result))
  
