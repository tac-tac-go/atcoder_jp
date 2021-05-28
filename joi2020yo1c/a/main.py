import numpy as np
x,l,r = map(int,input().split())
l_r = list(range(l,r+1))
print(l_r[np.argmin(list((map(lambda li:abs(x-li),l_r))))])