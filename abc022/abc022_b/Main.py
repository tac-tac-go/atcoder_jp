from collections import Counter
N = int(input())
R = Counter([int(input()) for _ in range(N)])
print(sum(list(map(lambda x:x[1]-1,R.items()))))