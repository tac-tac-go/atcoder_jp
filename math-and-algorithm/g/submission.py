a,x,y = map(int,input().split())
count = 0
for i in range(1,a+1):
  if i%x==0 or i%y==0:
    count+=1
print(count)
