n = int(input())
an = list(map(int,input().split()))
now = 0
result = [now]
for i in an:
  now+=i
  now%=360
  result.append(now)
result = sorted(result)

ans = 0
for i in range(n-1):
  ans = max(ans,result[i+1]-result[i])

ans = max(ans,360-result[-1])
print(ans)
