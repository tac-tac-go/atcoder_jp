import numpy as np
h,w = map(int,input().split())
s = np.array([list(input()) for i in range(h)])
count=0
for i in range(h):
  for j in range(0,w-1):
    if "".join(s[i,j:j+2])=="..":count+=1

for i in range(w):
  for j in range(0,h-1):
    if "".join(s[j:j+2,i])=="..":
      count+=1
print(count)