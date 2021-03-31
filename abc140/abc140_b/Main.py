N = input()
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
sum_val = B[A[0]-1]
for i in range(1,len(A)):
  if A[i]-1==A[i-1]:
    sum_val+=B[A[i]-1]+C[A[i-1]-1]
  else:
    sum_val+=B[A[i]-1]
print(sum_val)