s,p = map(int,input().split())
result = "No"
for n in range(1,int(p ** 0.5) + 1):
  if (p%n==0 and p/n+n==s):
    result = "Yes"
    break
print(result)