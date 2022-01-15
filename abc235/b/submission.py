n = int(input())
an = map(int,input().split())
result = 0
for i in an:
  if result < i:
    result=i
  else:
    break
print(result)
