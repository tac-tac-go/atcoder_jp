from itertools import permutations
n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]
path = list(range(2, n+1))
result = 0
for v in permutations(path, len(path)):
  path_i = [1] + list(v) + [1]
  count = 0
  for i in range(len(path_i)-1):
    count += t[path_i[i]-1][path_i[i+1]-1]
  if count == k:
      result += 1
print(result)
