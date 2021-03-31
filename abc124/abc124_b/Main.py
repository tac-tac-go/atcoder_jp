N = int(input())  
A = list(map(int,input().split()))
count=1
for i in range(1,len(A)):
  if A[i] >=max(A[:i]):
    count+=1
print(count)
