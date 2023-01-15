s = input()
result = []
from collections import Counter
for i in range(0,len(s)-1):
  result.append(s[i:i+2])
result_c = Counter(result)
result_f = {k:v for k,v in result_c.items() if max(result_c.values())==v}
print(sorted(result_f)[0])
