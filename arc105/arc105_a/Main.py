ABCD = list(map(int,input().split()))
result="No"
from itertools import combinations
for i in range(1,3):
  for s in combinations(ABCD, i):
    if sum(s)==sum(ABCD)-sum(s):
      print("Yes");exit()
print("No")