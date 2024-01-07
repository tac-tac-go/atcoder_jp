n,s,k = map(int,input().split())
arr = [map(int,input().split()) for i in range(n)]
result = 0
for p,q in arr:
  result += p*q
print(result) if result>=s else print(result+k)
  
