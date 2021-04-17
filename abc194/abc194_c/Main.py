N = int(input())
A = list(map(int,input().split()))
sum_c = 0
for i in range(1,N):
  for j in range(0,i):
      sum_c+=(A[i]-A[j])**2
print(sum_c)