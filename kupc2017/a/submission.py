n,k = map(int,input().split())
an = sorted(list(map(int,input().split())))[::-1]
if sum(an)<k:
  print(-1)
else:
  count=0
  value=0
  for a_i in an:
    value+=a_i
    count+=1
    if value>=k:break
  print(count)
  
  
  