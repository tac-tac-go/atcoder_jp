import itertools
n = int(input())
a = list(map(int,input().split()))
if sum(a)%n!=0:
  print("-1")
else:
  ave = sum(a)//n
  ans = 0
  a_c = list(itertools.accumulate(a))
  for i in range(n-1):
    if a_c[i]!=ave*(i+1):
      ans+=1
  print(ans)