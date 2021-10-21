n = int(input())
name = []
name3 = []
for _ in range(n):
  k = input()
  v = input().split()
  name.extend(v)
  name3.append(v)
name2 = list(set(name))
from collections import defaultdict
result = defaultdict(list)
for i in name2:
    result[i] = 0
result = dict(result)
for i in name3:
    for j in i:
        result[j] += 1
print(len(list(filter(lambda x: x == n, list(result.values())))))
