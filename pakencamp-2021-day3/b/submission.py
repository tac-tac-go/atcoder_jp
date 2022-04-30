n,x,y=map(int,input().split())
a=list(map(int,input().split()))
if sum(a)!=x+y:
  print('No')
  exit()

a=a+a[:-1]
l=0
r=0
s=0
while r<=2*n-2:
  while s<x and r<=2*n-2:
    s+=a[r]
    r+=1
  while s>x and r<=2*n-2:
    s-=a[l]
    l+=1
  if s==x:
    print('Yes')
    exit()
print('No')
