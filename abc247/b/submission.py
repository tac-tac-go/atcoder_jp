from collections import defaultdict
d1=defaultdict(int)
n=int(input())
lis=[]
for _ in range(n):
  s,t=input().split()
  lis.append((s,t))
  d1[s]+=1
  d1[t]+=1
for a,b in lis:
  if a==b:
    if d1[a]==2:
      continue
    else:
      print("No")
      exit()
  else:
    if d1[a]==1 or d1[b]==1:
      continue
    else:
      print("No")
      exit()
print("Yes")
