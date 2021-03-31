N = int(input())
result=[input() for i in range(N)]
ans="Yes"
for i in range(1,len(result)):
  if result[i] in result[:i] or result[i][0]!=result[i-1][-1]:
    ans="No"
    break
print(ans)