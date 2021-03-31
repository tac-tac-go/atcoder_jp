a,b,k = map(int,input().split())
result=[]
for i in range(0,k):
  if a+i<=b:
    result.append(a+i)
  if b-i>=a:
    result.append(b-i)

result = sorted(set(result))
result = list(map(str,result))
print('\n'.join(result))