n = int(input())
la = [input().split() for i in range(n)]
result = []
for la_i in la:
  l = la_i[0]
  a = ','.join(la_i[1:])
  result.append(a)
from collections import Counter
print(len(Counter(result)))
