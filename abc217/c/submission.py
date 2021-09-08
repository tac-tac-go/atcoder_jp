n = int(input())
result = [0]*n
pn = list(map(int, input().split()))
for i, v in enumerate(pn):
  result[v-1] = i+1
print(*result)
