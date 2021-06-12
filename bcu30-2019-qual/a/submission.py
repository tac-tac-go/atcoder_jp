n,p = map(int,input().split())
a = list(map(int,input().split()))
index=0
while p>=a[index]:
  p-=a[index]
  index+=1
  if index==len(a):break
print(index)