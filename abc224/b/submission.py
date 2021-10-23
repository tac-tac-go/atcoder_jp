import itertools
import numpy as np
h, w = map(int, input().split())
A = np.array([list(map(int, input().split())) for _ in range(h)])
bool = "Yes"
for i in list(itertools.combinations(range(h), 2)):
  for j in list(itertools.combinations(range(w), 2)):
    if A[i[0], j[0]] + A[i[1], j[1]] > A[i[1], j[0]] + A[i[0], j[1]]:
      bool = "No"
      break
  else:
      continue
  break
print(bool)
