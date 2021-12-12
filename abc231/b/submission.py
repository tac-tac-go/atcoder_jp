from collections import Counter
from collections import OrderedDict
n = int(input())
result = []
for i in range(n):
  s = input()
  result.append(s)
c = OrderedDict(sorted(Counter(result).items(), key=lambda x:x[1],reverse=True))
print(list(dict(c).keys())[0])
