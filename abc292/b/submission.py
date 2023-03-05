n,q = map(int,input().split())
count = [0]*n
for i in range(q):
  ni,qi = map(int,input().split())
  if ni==1:
    count[qi-1]+=1
  elif ni==2:
    count[qi-1]+=2
  else:
    if count[qi-1]>=2:
      print("Yes")
    else:
      print("No")
