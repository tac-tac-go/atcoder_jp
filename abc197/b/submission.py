import numpy as np
h,w,x,y = map(int,input().split())
array = []
for i in range(h):
	array.append(list(input()))
array = np.array(array)
#upper
count = 0
for i in range(x-1,-1,-1):
  if array[i,y-1]==".":
    count+=1
  else:
    break
#down
for i in range(x,h,1):
  if array[i,y-1]==".":
    count+=1
  else:
    break
#left
for i in range(y-2,-1,-1):
  if array[x-1,i]==".":
    count+=1
  else:
    break
#right
for i in range(y,w,1):
  if array[x-1,i]==".":
    count+=1
  else:
    break
print(count)
     
