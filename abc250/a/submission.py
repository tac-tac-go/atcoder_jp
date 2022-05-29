h,w = map(int,input().split())
r,c = map(int,input().split())
count = 0
for y in range(1,h+1):
  for x in range(1,w+1):
    if abs(y-r)+abs(x-c)==1:
      count+=1
print(count)
    
    
