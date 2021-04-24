import numpy as np
h,w = map(int,input().split())
a = np.array([list(input()) for i in range(h)])
result=[]
for i in range(h):
  if (a[i,:]=="#").any():
    result.append(list(a[i,:]))
b=np.array(result)

result2=[]
for j in range(w):
  if (a[:,j]=="#").any():
    result2.append(list(b[:,j]))
c = np.array(result2).T
for k in range(len(c)):
  print("".join(c[k,:]))