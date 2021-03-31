N,X= map(int,input().split())
S = list(input())
for s in S:
  if s=='o':X+=1
  else:
    if X>0:X-=1
print(X)