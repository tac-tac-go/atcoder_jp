from itertools import product
N, M, X = map(int, input().split())
CA = [list(map(int, input().split())) for _ in range(N)]
items = list(range(N))
n = len(items)
result = True
count = 10**100
for bits in product([0, 1], repeat=n):
    comb = [x for x, bit in zip(items, bits) if bit == 1]
    CN = 0
    AN = [0]*M
    for i in comb:
        CN += CA[i][0]
        AN = [x+y for (x, y) in zip(AN, CA[i][1:])]

    if(min(AN) >= X):
        result = False
        if count > CN:
            count = CN
print(-1 if result else count)
