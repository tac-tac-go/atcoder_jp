import numpy as np
array = np.array([list(input()) for i in range(10)])
x = np.where(array=="#")[0]
y = np.where(array=="#")[1]
x1,x2 = x[0],x[-1]
y1,y2 = y[0],y[-1]
print(x1+1,x2+1)
print(y1+1,y2+1)
