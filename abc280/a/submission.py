import numpy as np
h,w = map(int,input().split())
array = np.array([list(input()) for i in range(h)])
print(len(np.where(array=="#")[0]))
