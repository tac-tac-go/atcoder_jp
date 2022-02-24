n,x = map(int,input().split())
an = sorted(map(int,input().split()))
count=0
index=0
while count<=x and index<=n-1:
  if count+an[index]<=x:
    count+=an[index]
    index+=1
  else:
    break
#print(count,x,index)
#print(index) if x-count==0 else print(index-1)
if n==index:
  if x-count!=0:
    print(index-1)
  else:
    print(index)
else:
  print(index)
