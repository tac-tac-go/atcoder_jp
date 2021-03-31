import numpy as np
N = int(input())
A = list(map(int,input().split()))
average = sum(A)/len(A)
print(np.argmin(list(map(lambda x:abs(x-average),A))))