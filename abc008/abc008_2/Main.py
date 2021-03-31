from collections import Counter
N = int(input())
L = Counter([input() for i in range(N)])
print(L.most_common()[0][0])
  