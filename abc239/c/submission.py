import sys
x1,y1,x2,y2 = map(int,input().split())
result1 = []
posi = [[-1,2],[-2,1],[1,2],[2,1],[-1,-2],[-2,-1],[1,-2],[2,-1]]
array1 = [[i+x1,j+y1] for i,j in posi]
array2 = [[i+x2,j+y2] for i,j in posi]
flag = False
for i in array1:
  for j in array2:
    if i==j:	
      	flag=True
  else:
    continue
  break
print("Yes") if flag else print("No")

  
