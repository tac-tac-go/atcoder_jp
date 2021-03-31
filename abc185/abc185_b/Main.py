n,m,t = map(int,input().split())
n1 = n
ab = [list(map(int,input().split())) for i in range(m)]
n-=ab[0][0]
result="Yes"
if n>0:
  for i in range(m-1):
    n+=(ab[i][1]-ab[i][0])
    n=min(n,n1)
    n-=(ab[i+1][0]-ab[i][1])
    if n<=0:result="No";break

  n+=ab[-1][1]-ab[-1][0]
  n=min(n,n1)
  n-=(t-(ab[-1][1]))       
  if n<=0:result="No";
  print(result)

else:
  print("No")