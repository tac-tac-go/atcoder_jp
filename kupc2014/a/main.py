import numpy as np
ab = list(map(int,input().split()))
a = ab[:3]
a.sort()
b = ab[3:]
b.sort()
score=0
for i in a:
  min_index = np.argmin(map(lambda x:abs(x-i),b))
  score+=abs(i-b[min_index])
  b.pop(min_index)
print(score)