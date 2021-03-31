A = input()
B = input()
result="No"
for i in range(len(A)):
  A = A[-1]+A[:-1]
  if A ==B:result="Yes";break
print(result)