import numpy as np
n = int(input())
s = np.array([list(input()) for i in range(n)])
for i in range(n):
    print("".join(s[:,i][::-1]))