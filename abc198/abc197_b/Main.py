n = int(input())
for i in range(len(str(n))):
  if n%10==0:n=n//10
  else:break
print("Yes") if str(n)[::-1]==str(n) else print("No")