import numpy as np
v1,v2 = map(int,input().split())

if [v1,v2]==[1,0]:
  print(1,0)
elif [v1,v2]==[0,1]:
  print(0,1)
else:
  a = np.array([0, 0])
  b = np.array([v1, v2])
  vec = b - a
  arc = np.arctan2(vec[0], vec[1])
  print(np.sin(arc),np.cos(arc))

