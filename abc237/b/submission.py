import numpy as np
h,w = map(int,input().split())
array = np.array([list(map(int,input().split())) for i in range(h)]).T
[print(*v) for v in array]
