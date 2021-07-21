l = [10,5,3,2,1,0]
 
n = int(input())
ans = [0]*n
for i in range(n):
  s = int(input())
  ans[s-1]= 10**4*l[min(i,5)]
for i in ans:
  print(i)